"""Mesmo modelo linear binário, com APIs nativas de Gurobi e SCIP."""
import math
from time import perf_counter
from pathlib import Path
from .heuristic import ffd
from .validation import validate


def finite(value):
    return float(value) if math.isfinite(value) and abs(value) < 1e19 else None


def solve(instance, method, time_limit=10, reduce=True, log_path=None):
    if method not in ('gurobi', 'scip'):
        raise ValueError('Solver deve ser gurobi ou scip')
    if not math.isfinite(time_limit) or time_limit <= 0:
        raise ValueError('Limite de tempo deve ser positivo e finito')
    start = perf_counter()
    result = dict(instance_id=instance.id, method=method, status='error', raw_status=None,
                  objective=None, bins=[], lower_bound=None, native_gap=None, gap_percent=None,
                  build_seconds=None, optimization_seconds=None, total_seconds=None, validated=False,
                  parameters={'time_limit':time_limit, 'threads':1, 'seed':0, 'mip_gap':0,
                              'reduce_candidates':reduce, 'warm_start':False})
    if not instance.items:
        result.update(status='optimal', raw_status='empty_instance_convention', objective=0,
                      lower_bound=0, native_gap=0, gap_percent=0, build_seconds=0,
                      optimization_seconds=0, total_seconds=perf_counter()-start, validated=True)
        return result
    model = None
    env = None
    try:
        if method == 'gurobi':
            import gurobipy as gp
            env = gp.Env(empty=True)
            env.setParam('OutputFlag', 0)
            env.start()
            model = gp.Model('survival', env=env)
            model.Params.TimeLimit = time_limit
            model.Params.Threads = 1
            model.Params.Seed = 0
            model.Params.MIPGap = 0
            model.Params.MIPGapAbs = 0
            if log_path:
                model.Params.OutputFlag = 1
                model.Params.LogToConsole = 0
                model.Params.LogFile = str(log_path)
            addvar = lambda name, ub=1: model.addVar(vtype=gp.GRB.BINARY, ub=ub, name=name)
            add = model.addConstr
            qsum = gp.quicksum
            result['version'] = '.'.join(map(str,gp.gurobi.version()))
        else:
            import pyscipopt as sc
            model = sc.Model('survival')
            model.hideOutput()
            model.setRealParam('limits/time', time_limit)
            model.setRealParam('limits/gap', 0)
            model.setRealParam('limits/absgap', 0)
            model.setIntParam('parallel/maxnthreads', 1)
            model.setIntParam('randomization/randomseedshift', 0)
            if log_path:
                model.setLogfile(str(log_path))
            addvar = lambda name, ub=1: model.addVar(vtype='B', ub=ub, name=name)
            add = model.addCons
            qsum = sc.quicksum
            result['version'] = f'PySCIPOpt {sc.__version__}; SCIP {model.getMajorVersion()}.{model.getMinorVersion()}.{model.getTechVersion()}'
        chests = list(instance.chests)
        if reduce:
            heuristic = ffd(instance)
            if heuristic['objective'] is not None:
                chests = sorted(chests, key=lambda b: -b['capacity'])[:heuristic['objective']]
        n, m = len(instance.items), len(chests)
        result['candidate_chests'] = m
        x = {(i,j):addvar(f'x_{i}_{j}', int(instance.items[i]['size'] <= chests[j]['capacity']))
             for i in range(n) for j in range(m)}
        y = {j:addvar(f'y_{j}') for j in range(m)}
        model.setObjective(qsum(y.values()), gp.GRB.MINIMIZE if method == 'gurobi' else 'minimize')
        for i in range(n):
            add(qsum(x[i,j] for j in range(m)) == 1, name=f'assign_{i}')
        for j in range(m):
            add(qsum(instance.items[i]['size']*x[i,j] for i in range(n)) <= chests[j]['capacity']*y[j], name=f'capacity_{j}')
            add(y[j] <= qsum(x[i,j] for i in range(n)), name=f'nonempty_{j}')
            for i in range(n):
                add(x[i,j] <= y[j], name=f'link_{i}_{j}')
        index = {item['id']:i for i,item in enumerate(instance.items)}
        # Sorted order avoids dependence on Python hash randomization.
        for e,(a,b) in enumerate(sorted(tuple(sorted(edge)) for edge in instance.conflicts)):
            for j in range(m):
                add(x[index[a],j] + x[index[b],j] <= 1, name=f'conflict_{e}_{j}')
        previous = {}
        for j, chest in enumerate(chests):
            c = chest['capacity']
            if c in previous:
                add(y[previous[c]] >= y[j], name=f'symmetry_{j}')
            previous[c] = j
        result['build_seconds'] = perf_counter()-start
        model.optimize()
        if method == 'gurobi':
            raw = model.Status
            has_solution = model.SolCount > 0
            optimal, infeasible = raw == gp.GRB.OPTIMAL, raw == gp.GRB.INFEASIBLE
            result['raw_status'] = raw
            result['optimization_seconds'] = model.Runtime
            result['lower_bound'] = finite(model.ObjBound) if not infeasible else None
            if has_solution:
                objective, gap, value = model.ObjVal, model.MIPGap, lambda v:v.X
        else:
            raw = str(model.getStatus())
            has_solution = model.getNSols() > 0
            optimal, infeasible = raw == 'optimal', raw == 'infeasible'
            result['raw_status'] = raw
            result['optimization_seconds'] = model.getSolvingTime()
            result['lower_bound'] = finite(model.getDualbound()) if not infeasible else None
            if has_solution:
                objective, gap, value = model.getObjVal(), model.getGap(), model.getVal
        result['status'] = 'optimal' if optimal else 'infeasible' if infeasible else 'feasible' if has_solution else 'no_solution'
        if has_solution:
            result['objective'] = round(objective)
            result['native_gap'] = finite(gap)
            for j in range(m):
                allocated = [i for i in range(n) if value(x[i,j]) > 0.5]
                if (value(y[j]) > 0.5) != bool(allocated):
                    raise RuntimeError('Ativação inconsistente')
                if allocated:
                    result['bins'].append(dict(chest_id=chests[j]['id'],items=[instance.items[i]['id'] for i in allocated],
                                               load=sum(instance.items[i]['size'] for i in allocated)))
            lb = result['lower_bound']
            if lb is not None:
                result['gap_percent'] = 100*max(0,objective-lb)/max(abs(objective),1)
            result['validated'] = validate(instance, result)
    except ImportError as exc:
        result.update(status='unavailable', error=str(exc))
    except Exception as exc:
        # Only known license errors are availability; bugs remain errors.
        code = getattr(exc, 'errno', None)
        unavailable = method == 'gurobi' and code in (10009, 10010)
        result.update(status='unavailable' if unavailable else 'error', error=str(exc), error_code=code,
                      objective=None, bins=[], validated=False)
    finally:
        result['total_seconds'] = perf_counter()-start
        if model is not None:
            if method == 'gurobi':
                model.dispose()
            else:
                model.freeProb()
        if env is not None:
            env.dispose()
    return result

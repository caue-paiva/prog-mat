import itertools
import random
import pytest
from survival_packing.data import parse
from survival_packing.heuristic import ffd
from survival_packing.exact import solve
from survival_packing.validation import validate


def data(weights, capacities, edges=()):
    return dict(instance_id='test',items=[dict(id=str(i),size=w,category='a') for i,w in enumerate(weights)],
                chests=[dict(id=str(j),capacity=c) for j,c in enumerate(capacities)],
                conflicts=[list(map(str,e)) for e in edges])


def oracle(d):
    """Enumeração independente de todas as funções item -> baú (somente n pequeno)."""
    best=None
    for assignment in itertools.product(range(len(d['chests'])),repeat=len(d['items'])):
        if any(sum(d['items'][i]['size'] for i,b in enumerate(assignment) if b==j)>c['capacity'] for j,c in enumerate(d['chests'])):
            continue
        if any(assignment[int(a)]==assignment[int(b)] for a,b in d['conflicts']):
            continue
        used=len(set(assignment))
        best=used if best is None else min(best,used)
    return best


CASES=[([],[],0),([10],[10],1),([6,4,5,5],[10]*4,2),([6,6,6],[10]*3,3),
       ([11],[10],None),([5,5,5],[10],None),([8,6,4],[10,8],2)]

@pytest.mark.parametrize('weights,caps,optimum',CASES)
@pytest.mark.parametrize('method',['scip','gurobi'])
def test_known(weights,caps,optimum,method):
    pytest.importorskip('pyscipopt' if method=='scip' else 'gurobipy')
    ins=parse(data(weights,caps))
    r=solve(ins,method)
    if r['status']=='unavailable': pytest.skip(r['error'])
    assert r['objective']==optimum, r
    assert r['status']==('optimal' if optimum is not None else 'infeasible'),r
    if optimum is not None: assert validate(ins,r)

@pytest.mark.parametrize('method',['scip','gurobi'])
def test_against_exhaustive(method):
    pytest.importorskip('pyscipopt' if method=='scip' else 'gurobipy')
    rng=random.Random(48)
    for _ in range(12):
        d=data([rng.randint(1,7) for i in range(5)], [rng.randint(5,12) for j in range(3)],
               [(i,k) for i in range(5) for k in range(i+1,5) if rng.random()<.25])
        expected=oracle(d)
        for reduction in [False,True]:
            r=solve(parse(d),method,reduce=reduction)
            if r['status']=='unavailable': pytest.skip(r['error'])
            assert r['status'] in ('optimal','infeasible'),r
            assert r['objective']==expected,r


def test_ffd_suboptimal_and_failure():
    assert ffd(parse(data([6,5,3,2,2,2],[10]*6)))['objective']==3
    d=data([4,3,3],[6,4])
    assert oracle(d)==2
    assert ffd(parse(d))['status']=='heuristic_failed'


def test_category_self_conflict():
    d=data([1,1],[5,5]);d['incompatible_categories']=[['a','a']]
    assert ffd(parse(d))['objective']==2
    r=solve(parse(d),'scip')
    assert r['objective']==2,r

@pytest.mark.parametrize('mutation', ['duplicate','zero','negative','float','nan','bool','unknown_conflict'])
def test_invalid(mutation):
    d=data([1,2],[10])
    if mutation=='duplicate':d['items'][1]['id']='0'
    elif mutation=='unknown_conflict':d['conflicts']=[['0','missing']]
    else:d['items'][0]['size']={'zero':0,'negative':-1,'float':1.2,'nan':float('nan'),'bool':True}[mutation]
    with pytest.raises(ValueError):parse(d)

@pytest.mark.parametrize('mutation',['omitted','duplicate','load','objective','capacity','conflict','chest','empty'])
def test_validator_rejects(mutation):
    ins=parse(data([6,4,5],[10,10],[(0,2)]));r=ffd(ins)
    if mutation=='omitted':r['bins'][0]['items'].pop()
    elif mutation=='duplicate':r['bins'][0]['items'].append('0')
    elif mutation=='load':r['bins'][0]['load']+=1
    elif mutation=='objective':r['objective']+=1
    elif mutation=='capacity':r['bins']=[dict(chest_id='0',items=['0','1','2'],load=15)];r['objective']=1
    elif mutation=='conflict':
        ins=parse(data([1,1],[10],[(0,1)]));r=dict(bins=[dict(chest_id='0',items=['0','1'],load=2)],objective=1)
    elif mutation=='chest':r['bins'][0]['chest_id']='missing'
    else:r['bins'].append(dict(chest_id='1',items=[],load=0))
    with pytest.raises(ValueError):validate(ins,r)


def test_all_conflict_and_determinism():
    d=data([1]*4,[10]*4,itertools.combinations(range(4),2))
    ins=parse(d)
    assert ffd(ins)['objective']==4
    assert ffd(ins)['bins']==ffd(ins)['bins']

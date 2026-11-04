import argparse
import csv
import hashlib
import importlib.metadata
import json
import os
import platform
from pathlib import Path
from .data import read, dump
from .generate import suite
from .heuristic import ffd
from .exact import solve
from .validation import validate


def run(instance, method, args, log=None):
    return ffd(instance) if method == 'ffd' else solve(instance,method,args.time_limit,not args.no_reduction,log)


def metadata(args):
    versions = {}
    for name in ['gurobipy','pyscipopt','numpy']:
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    cpu = platform.processor()
    if Path('/proc/cpuinfo').exists():
        cpu = next((s.split(':',1)[1].strip() for s in Path('/proc/cpuinfo').read_text().splitlines() if s.startswith('model name')), cpu)
    return dict(python=platform.python_version(),platform=platform.platform(),cpu=cpu,
                logical_cpus=os.cpu_count(), packages=versions, arguments=vars(args),
                base_commit='a2943f1ea499052a24b09e428c8ccc51956a7124')


def main():
    p = argparse.ArgumentParser(description='Bin packing com capacidades heterogêneas e conflitos')
    sub = p.add_subparsers(dest='command',required=True)
    g=sub.add_parser('generate'); g.add_argument('--out',default='instances')
    for name in ['solve','benchmark']:
        s=sub.add_parser(name)
        s.add_argument('--time-limit',type=float,default=10)
        s.add_argument('--no-reduction',action='store_true')
        s.add_argument('--out',required=True)
        if name == 'solve':
            s.add_argument('instance');s.add_argument('--method',choices=['ffd','scip','gurobi'],required=True)
        else:
            s.add_argument('--instances',default='instances')
            s.add_argument('--methods',nargs='+',choices=['ffd','scip','gurobi'],default=['ffd','scip','gurobi'])
    v=sub.add_parser('validate');v.add_argument('instance');v.add_argument('result')
    args=p.parse_args()
    if args.command == 'generate':
        suite(args.out)
    elif args.command == 'validate':
        validate(read(args.instance),json.loads(Path(args.result).read_text()))
        print('Solução válida')
    elif args.command == 'solve':
        Path(args.out).parent.mkdir(parents=True,exist_ok=True)
        r=run(read(args.instance),args.method,args,str(Path(args.out).with_suffix('.log')))
        dump(r,args.out)
        print(r['status'],r['objective'])
        if r['status'] in ('error','unavailable'):
            raise SystemExit(2)
    else:
        out=Path(args.out)
        if out.exists() and any(out.iterdir()):
            p.error('Use diretório de saída vazio para preservar resultados anteriores')
        out.mkdir(parents=True,exist_ok=True)
        paths=sorted(Path(args.instances).glob('*.json'))
        if not paths:
            p.error('Nenhuma instância encontrada')
        dump(metadata(args),out/'environment.json')
        records=[]
        for path in paths:
            instance=read(path)
            for method in args.methods:
                name=f'{path.stem}_{method}'
                r=run(instance,method,args,str(out/(name+'.log')))
                r.update(n=len(instance.items),input_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
                dump(r,out/(name+'.json'))
                records.append(r)
                print(name,r['status'],r['objective'],flush=True)
                fields=['instance_id','n','method','status','raw_status','objective','lower_bound','gap_percent',
                        'native_gap','build_seconds','optimization_seconds','total_seconds','validated','input_sha256','error']
                with (out/'summary.csv').open('w',newline='') as f:
                    writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(records)
        if any(r['status']=='error' for r in records):
            raise SystemExit(2)


if __name__ == '__main__':
    main()

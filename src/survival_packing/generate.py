import random
from .data import dump
from pathlib import Path

CATEGORIES = ['madeira','pedra','metal','alimento','pocao','explosivo','combustivel']
RULES = [[safe, hazardous] for safe in ['alimento','pocao'] for hazardous in ['explosivo','combustivel']]


def generate(n, seed):
    if n < 20:
        raise ValueError('Gerador experimental exige n >= 20')
    rng = random.Random(seed)
    large, medium = max(1,n//10), max(1,n//5)
    caps = [20]*large + [15]*medium + [10]*(n-large-medium)
    return dict(instance_id=f'game_n{n}_s{seed}', categories=CATEGORIES,
                unit='UA', source='synthetic', generator_version=1, seed=seed,
                items=[dict(id=f'i{i:03d}',size=rng.randint(1,9),category=rng.choice(CATEGORIES)) for i in range(n)],
                chests=[dict(id=f'b{j:03d}',capacity=c) for j,c in enumerate(caps)],
                incompatible_categories=RULES, conflicts=[])


def suite(directory):
    for n in [20,50,100,200]:
        for seed in [11,22,33]:
            data = generate(n,seed)
            dump(data, Path(directory)/(data['instance_id']+'.json'))

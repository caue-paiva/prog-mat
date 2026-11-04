"""Contrato de dados: inteiros positivos, IDs únicos e conflitos simétricos."""
from dataclasses import dataclass
from itertools import combinations
import json
from pathlib import Path


@dataclass(frozen=True)
class Instance:
    id: str
    items: tuple
    chests: tuple
    conflicts: frozenset


def parse(data):
    def require(ok, message):
        if not ok:
            raise ValueError(message)
    require(isinstance(data, dict), 'Instância deve ser objeto JSON')
    require(isinstance(data.get('instance_id'), str) and bool(data['instance_id']), 'instance_id inválido')
    for key, size in [('items', 'size'), ('chests', 'capacity')]:
        require(isinstance(data.get(key), list), f'{key} deve ser lista')
        ids = set()
        for row in data[key]:
            require(isinstance(row, dict), f'{key}: objeto esperado')
            require(isinstance(row.get('id'), str) and bool(row['id']), 'ID inválido')
            require(row['id'] not in ids, 'ID duplicado')
            ids.add(row['id'])
            require(type(row.get(size)) is int and 0 < row[size] <= 10**9,
                    f'{size} deve ser inteiro positivo <= 10^9')
            if key == 'items':
                require(isinstance(row.get('category'), str) and bool(row['category']), 'Categoria inválida')
    items, chests = tuple(dict(x) for x in data['items']), tuple(dict(x) for x in data['chests'])
    categories = set(data.get('categories', [x['category'] for x in items]))
    require(all(isinstance(c, str) for c in categories), 'Categorias inválidas')
    require(all(x['category'] in categories for x in items), 'Categoria não declarada')
    rules = set()
    for pair in data.get('incompatible_categories', []):
        require(isinstance(pair, list) and len(pair) == 2 and all(c in categories for c in pair), 'Regra de categoria inválida')
        rules.add(frozenset(pair))
    edges = {frozenset((a['id'], b['id'])) for a,b in combinations(items, 2)
             if frozenset((a['category'], b['category'])) in rules}
    ids = {x['id'] for x in items}
    for pair in data.get('conflicts', []):
        require(isinstance(pair, list) and len(pair) == 2 and all(i in ids for i in pair)
                and pair[0] != pair[1], 'Conflito de IDs inválido')
        edges.add(frozenset(pair))
    return Instance(data['instance_id'], items, chests, frozenset(edges))


def read(path):
    return parse(json.loads(Path(path).read_text(encoding='utf-8')))


def dump(value, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')

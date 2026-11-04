"""Verificador independente: não consulta variáveis nem código dos solvers."""
from collections import Counter
from itertools import combinations


def validate(instance, result):
    items = {i['id']: i for i in instance.items}
    chests = {b['id']: b for b in instance.chests}
    seen, used = [], []
    for entry in result['bins']:
        bid, ids = entry['chest_id'], entry['items']
        if bid not in chests or bid in used or not ids:
            raise ValueError('Baú desconhecido, repetido ou vazio')
        if any(i not in items for i in ids):
            raise ValueError('Item desconhecido')
        used.append(bid)
        seen.extend(ids)
        load = sum(items[i]['size'] for i in ids)
        if load > chests[bid]['capacity'] or load != entry['load']:
            raise ValueError('Capacidade excedida ou carga incorreta')
        if any(frozenset(pair) in instance.conflicts for pair in combinations(ids, 2)):
            raise ValueError('Itens incompatíveis no mesmo baú')
    if Counter(seen) != Counter(items.keys()):
        raise ValueError('Itens omitidos ou duplicados')
    if type(result['objective']) is not int or result['objective'] != len(used):
        raise ValueError('Objetivo incorreto')
    return True


def volume_bound(instance):
    """Menor k cuja soma das k maiores capacidades cobre todo o volume."""
    weight = sum(i['size'] for i in instance.items)
    if not weight:
        return 0
    capacity = 0
    for k, b in enumerate(sorted(instance.chests, key=lambda b: -b['capacity']), 1):
        capacity += b['capacity']
        if capacity >= weight:
            return k
    return None  # inventário insuficiente por volume

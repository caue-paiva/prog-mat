from time import perf_counter
from .validation import validate, volume_bound


def ffd(instance):
    start = perf_counter()
    opened = []
    unused = sorted(range(len(instance.chests)), key=lambda j: (-instance.chests[j]['capacity'], j))
    complete = True
    for item in sorted(instance.items, key=lambda i: -i['size']):
        chosen = None
        for entry in opened:
            if (entry['load'] + item['size'] <= instance.chests[entry['_j']]['capacity']
                and all(frozenset((item['id'], other)) not in instance.conflicts for other in entry['items'])):
                chosen = entry
                break
        if chosen is None:
            j = next((j for j in unused if instance.chests[j]['capacity'] >= item['size']), None)
            if j is None:
                complete = False
                break
            unused.remove(j)
            chosen = {'_j': j, 'chest_id': instance.chests[j]['id'], 'items': [], 'load': 0}
            opened.append(chosen)
        chosen['items'].append(item['id'])
        chosen['load'] += item['size']
    bins = [{k:v for k,v in entry.items() if k != '_j'} for entry in opened] if complete else []
    bound = volume_bound(instance)
    objective = len(bins) if complete else None
    result = dict(instance_id=instance.id, method='ffd', status='feasible' if complete else 'heuristic_failed',
                  raw_status='complete' if complete else 'no_complete_assignment', objective=objective,
                  bins=bins, lower_bound=bound, native_gap=None, gap_percent=None,
                  distance_to_bound_percent=(100*(objective-bound)/bound if complete and bound else 0 if complete else None),
                  optimization_seconds=None, build_seconds=None, total_seconds=perf_counter()-start,
                  validated=False)
    if complete:
        result['validated'] = validate(instance, result)
    return result

map_ = ''
paths = {i[0]: i[1:] for i in map_.split(' ')}


def merge_subarrays(arr):
    arr_ = []
    for el in arr:
        if isinstance(el, list):
            arr_.extend(merge_subarrays(el))
    return arr_ if arr_ else arr


def fix_array(arr):
    return [i for i in arr if isinstance(i, str)]


def get_all_paths(path, dest, excluded=''):
    if path[-1] in excluded or len(path)>len(set(path)):
        return 0
    if path[-1]==dest:
        return path
    return fix_array(merge_subarrays([get_all_paths(path+v, dest, excluded) for v in paths[path[-1]]]))


count_paths = lambda path, dest, excluded='': len(get_all_paths(path, dest, excluded))


def count_round_paths(dest, excluded=''):
    tmp1 = [p for p, ps in paths.items() if dest in ps]
    tmp = [count_paths(*s, excluded=excluded) for s in [dest+vtx for vtx in tmp1]]
    return sum(tmp)

def min_child(v, heap):
    l = 2*v + 1
    r = 2*v + 2

    has_l = l < len(heap)
    has_r = r < len(heap)

    if has_l and not has_r:
        return l

    if has_r:
        if heap[l] > heap[r]:
            return r
        else:
            return l
    return None

def insert(heap, item):
    idx = len(heap)
    heap += [item]

    parent = (idx - 1) // 2
    while parent >= 0 and heap[parent] < heap[idx]:
        heap[parent], heap[idx] = heap[idx], heap[parent]

        idx = parent
        parent = (idx - 1) // 2

def extract_min(heap):
    res = heap[0]
    heap[0] = heap[-1]
    del heap[-1]

    idx = 0
    c = min_child(idx, heap)
    while c != None:
        heap[c], heap[idx] = heap[idx], heap[c]
        idx = c
        c = min_child(idx, heap)
    return res

def heap_sort(lst):
    heap = []
    for i in lst:
        insert(heap, i)

    sorted = []
    while len(heap) > 0:
        sorted.append(extract_min(heap))
    return sorted

lst = [1, 2, 3, 4, 5, 6]
print(lst)
print(heap_sort(lst))

def simple_binary(lst, target):
    idx = len(lst) // 2
    if lst[idx] == target:
        return idx

    if lst[idx] > target:
        return simple_binary(lst[:idx], target)

    if lst[idx] < target:
        return simple_binary(lst[idx:], target) + idx

    return None

# Doesn't work :(
def advanced_binary(lst, target, lo, hi):
    lst = lst[lo:hi]
    idx = len(lst) // 2
    if lst[idx] == target:
        return idx

    if lst[idx] > target:
        return advanced_binary(lst, target, 0, idx)

    if lst[idx] < target:
        return advanced_binary(lst, target, idx, len(lst)-1) + idx

    return None

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(advanced_binary(lst, 1, 0, len(lst) - 1))
# print(advanced_binary(lst, 2, 0, len(lst) - 1))
# print(advanced_binary(lst, 3, 0, len(lst) - 1))
print(simple_binary(lst, 4))
print(simple_binary(lst, 5))

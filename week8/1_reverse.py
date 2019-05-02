def recursive_reverse(lst):
    if len(lst) == 1:
        return lst

    if len(lst) == 2:
        return [lst[1], lst[0]]

    return recursive_reverse(lst[len(lst)//2:]) + recursive_reverse(lst[:len(lst)//2])

print(recursive_reverse([1, 2, 3, 4, 5, 6, 7]))
print(recursive_reverse([1, 2, 3, 4, 5, 6]))
print(recursive_reverse([1, 2, 3, 4, 5]))
print(recursive_reverse([1, 2, 3, 4]))
print(recursive_reverse([1, 2, 3]))

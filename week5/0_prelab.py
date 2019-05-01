def print_elements(arr):
    for i in range(len(arr)):
        print("At index {} is the element {}.".format(i, arr[i]))

def min_index(arr, elem = None):
    idx = 0
    for i in range(len(arr)):
        v1 = arr[i]
        v2 = arr[idx]
        if elem != None:
            v1 = v1[elem]
            v2 = v2[elem]
        if v1 < v2:
            idx = i
    return idx

# To support tuples, pass elem as the index in the tuple.
def selection_sort(arr, elem = None):
    for i in range(len(arr)):
        j = min_index(arr[i:], elem) + i
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [7, 3, 5, 4]
arr = [("dog", 300), ("cat", 350), ("bird", 120)]
print_elements(arr)
print_elements(selection_sort(arr, 1))

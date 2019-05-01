def parse_file(file):
    res = []
    with open(file, "r") as f:
        for line in f:
            s = line.split(",")
            res.append([int(s[0]), float(s[1])])
    return res

def print_list(data):
    for d in data:
        print("{} kms, ${}".format(d[0], d[1]))

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

file = input("file> ")
data = parse_file(file)
while True:
    print("enter choice (print, sort1, sort2, quit)")
    cmd = input("> ")

    if cmd == "quit":
        break
    if cmd == "print":
        print_list(data)
    if cmd == "sort1":
        selection_sort(data, 0)
    if cmd == "sort2":
        selection_sort(data, 1)

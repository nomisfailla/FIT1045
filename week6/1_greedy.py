import copy

def process_file(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            data.append((int(line[0].strip("kg")), int(line[1].strip("$"))))
    return data

def get_sort_key(x):
    return x[0]

# Trys to find a optimal solution by taking the most items possible.
def greedy_items(data, capacity):
    old = copy.deepcopy(data)
    # Sort the data based on the weight (element[0]), in ascending order.
    data.sort(key = get_sort_key)
    result = []
    used = 0
    for i in range(len(data)):
        if data[i][0] <= capacity - used:
            used += data[i][0]
            # Get the index of the data in the original array to return.
            result.append(old.index(data[i]))

    return result

data = process_file(input("file> "))
cap = int(input("capacity> "))
res = greedy_items(data, cap)
print(data)
amt = 0
for i in res:
    amt += data[i][1]
print(str(res) + " = $" + str(amt))

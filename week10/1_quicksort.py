import random

def partition(L):
    z = 0
    p = L[z]
    left, right = [], []
    for e in L[z+1:]:
        if e < p:
           left.append(e)
        if e >= p:
            right.append(e)

    return p, left, right

def quicksort(L):
    if len(L) <= 1:
        return L
    else:
        p, l, r = partition(L)
        return quicksort(l) + [p] + quicksort(r)

l = []
for i in range(8):
    l.append(random.randrange(20))

print(l)
print(quicksort(l))

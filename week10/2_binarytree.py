def tree_count(T, v):
    if v == None:
        return 0

    l = T[v][0]
    r = T[v][1]

    return 1 + tree_count(T, l) + tree_count(T, r)

def balance(T, v):
    return tree_count(T, T[v][0]) - tree_count(T, T[v][1])

tree = [(2, 1), (3 , None), (5, 4), (None, None), (None, None), (None, None)]
print(tree_count(tree, 0))
print(tree_count(tree, 1))
print(tree_count(tree, 2))
print(tree_count(tree, 3))

print(balance(tree, 0))

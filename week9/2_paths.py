def all_paths(M, u, v):
    def next_step(M, path, v, sols):
        if path[-1] == v:
            sols.append(path)
        else:
            for o in range(len(M)):
                if o not in path and M[o][path[-1]] == 1:
                    next_step(M, path + [o], v, sols)
    sols = []
    next_step(M, [u], v, sols)
    return sols

u = 0
v = 3
M = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
print(all_paths(M, u, v))

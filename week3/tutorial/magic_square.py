def is_magic(m):
    # Calculate the initial value
    test = 0
    for i in m[0]:
        test += i

    # Test the rows
    for l in m:
        sum = 0
        for i in l:
            sum += i
        if sum != test:
            return False

    # Test the columns
    for i in range(len(m)):
        sum = 0
        for j in range(len(m[i])):
            sum += m[j][i]
        if sum != test:
            return False

    # Test the diagonal
    sum = 0
    for i in range(len(m)):
        sum += m[i][i]
    if sum != test:
        return False

    return True

m = [[2, 2, 2],
     [2, 2, 2],
     [2, 2, 2]]

print(is_magic(m))

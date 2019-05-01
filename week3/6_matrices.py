def pretty_print(m):
    width = len(m[0])
    height = len(m)
    for i in range(height):
        row = "["
        for j in range(width):
            row = row + " " + str(m[i][j])
        row = row + " ]"
        print(row)

def vectorise(m, col):
    height = len(m)
    res = [0]*height
    for i in range(height):
        res[i] = m[i][col]
    return res

def transpose(m):
    width = len(m[0])
    height = len(m)
    new = []
    for i in range(width):
        new.append(vectorise(m, i))
    return new

def cross(v1, v2):
    res = 0
    for i in range(len(v1)):
        res = res + (v1[i] * v2[i])
    return res

def multiply(m, v):
    res = [0] * len(v)
    for i in range(len(res)):
        res[i] = cross(v, m[i])
    return res

matrix = [
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

#print(vectorise(matrix, 0))

vector1 = [4,  5, 7, 9]
vector2 = [7, -2, 8, 9]
#print(cross(vector1, vector2))

#print(multiply(matrix, vector1))

transposed = transpose(matrix)

multiplied = multiply(matrix, vector1);

print("original")
pretty_print(matrix)

print("transposed")
pretty_print(transposed)

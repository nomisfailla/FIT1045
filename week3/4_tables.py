res = []

for i in range(5):
    numbers = input("Enter some numbers: ")
    numbers = numbers.split()
    numbers = list(map(float, numbers))
    res.append(numbers)

print(res)

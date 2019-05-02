def simple_recursive_power(x, n):
    if n == 1:
        return x

    return x * simple_recursive_power(x, n - 1)

calls = 0

def advanced_recursive_power(x, n):
    global calls
    calls += 1

    if n == 1: return x
    if n == 2: return x * x

    return advanced_recursive_power(x, n // 2) * advanced_recursive_power(x, n - (n // 2))

print(simple_recursive_power(4, 2))
print(simple_recursive_power(2, 3))
print(simple_recursive_power(2, 4))

print("advanced")

calls = 0
print(advanced_recursive_power(2, 4))
print("in " + str(calls) + " calls")

calls = 0
print(advanced_recursive_power(2, 5))
print("in " + str(calls) + " calls")

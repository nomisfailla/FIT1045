#
# Simon Failla
# SID: 30661293
#

from math import pi
from math import sqrt

def basel(precision):
    i = 0
    acc = 0
    approx = 0
    while abs(pi - approx) >= precision:
        i = i + 1
        term = 1 / i**2;
        acc = acc + term
        approx = sqrt(6 * acc)

    return (approx, i)

def taylor(precision):
    i = 0
    acc = 0
    m = 1
    approx = 0
    while abs(pi - approx) >= precision:
        i = i + 1
        term = m * (1 /  ((i * 2) - 1))
        acc = acc + term
        approx = 4 * acc
        m = -m

    return (approx, i)

def wallis(precision):
    i = 0
    acc = 1
    approx = 0
    while abs(pi - approx) >= precision:
        i = i + 1
        i2 = i * 2
        term = (i2 * i2) / ((i2-1) * (i2+1))
        acc = acc * term
        approx = 2 * acc

    return (approx, i)

# Computes the nth digit of the fibonacci sequence.
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def spigot(precision):
    i = 0
    acc = 0
    approx = 0
    while pi - approx >= precision:
        i = i + 1
        term = 1
        for j in range(1, i + 1):
            term = term * (fib(j) / ((j * 2) - 1))
        acc = acc + term
        approx = 2 * acc

    return (approx, i)

# Utility function to sort the results array.
def get_result_key(x):
    return x[1]

def race(precision, algorithms):
    results = []
    for i, f in enumerate(algorithms):
        res = f(precision)
        results.append((i + 1, res[1]))
    results.sort(key = get_result_key)
    return results

def print_results(results):
    for r in results:
        print("Algorithm " + str(r[0]) + " completed in " + str(r[1]) + " steps.")

#print("wallis(0.2) = " + str(wallis(0.2)))
#print("basel(0.1)  = " + str(basel(0.1)))
#print("taylor(0.2) = " + str(taylor(0.2)))
#print("spigot(0.1) = " + str(spigot(0.1)))

#results = race(0.01, (taylor, wallis, basel))
#print_results(results)


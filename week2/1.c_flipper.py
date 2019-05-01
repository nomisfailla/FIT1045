from random import *

def flip_coin():
    v = randrange(0, 3)
    return v

n = input("How many times would you like to flip the coin? ")
n = int(n)

heads = 0
tails = 0
other = 0

for i in range(n):
    v = flip_coin()
    if v == 0:
        print("flipped heads")
        heads = heads + 1
    elif v == 1:
        print("flipped tails")
        tails = tails + 1
    elif v == 2:
        print("flipped other")
        other = other + 1

print("total heads: " + str(heads))
print("total tails: " + str(tails))
print("total other: " + str(other))

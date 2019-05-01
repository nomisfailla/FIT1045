from random import random

def flip_coin(bias):
    v = random()
    return v < bias

n = input("How many times would you like to flip the coin? ")
n = int(n)

heads = 0
tails = 0

for i in range(n):
    if flip_coin(0.6):
        print("flipped heads")
        heads = heads + 1
    else:
        print("flipped tails")
        tails = tails + 1

print("total heads: " + str(heads))
print("total tails: " + str(tails))

# print the ratio of heads to tails
# we expected this to be around 1.0 in the normal case of heads
# and tails. however, if we change the bias value, the ratio will
# deviate from 1.0
print("ratio of heads to tails: " + str(round(heads / tails, 4)))

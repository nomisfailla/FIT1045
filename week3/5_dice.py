from random import *

def roll_die():
    return randrange(1, 7)

def get_average(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return float(sum) / float(len(arr))

rolls = []
for i in range(1000):
    roll = roll_die()
    rolls.append(roll)

average = get_average(rolls)
print("Average roll: " + str(average))

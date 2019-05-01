start = input("where should i start? ")
stop = input("where should i stop? ")
div = input("valid i values are those divisible by... ")
start = int(start)
stop = int(stop)
div = int(div)

summation = 0
for i in range(start, stop+1):
    if i % div == 0:
        summation = summation + (2*i**2 + 4*i)

print("result: " + str(summation))

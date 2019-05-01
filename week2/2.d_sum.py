start = input("where should i start? ")
stop = input("where should i stop? ")
start = int(start)
stop = int(stop)

summation = 0
for i in range(start, stop+1):
    for j in range(1, i+1):
        summation = summation + (2*i**2 + 4*j)

print("the result for sum of the sums of 2i^2+4j from " + str(start) + " to " + str(stop) + " is: " + str(summation))

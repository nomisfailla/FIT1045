start = input("where should i start? ")
stop = input("where should i stop? ")
start = int(start)
stop = int(stop)

summation = 0
for i in range(start, stop+1):
    summation = summation + (3 * i)

print("result: " + str(summation))

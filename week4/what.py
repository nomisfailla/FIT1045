import math

def while_loop(data, condition, body):
    for i in range(0, 9223372036854775807):
        if not condition([i, data]):
            return
        body([i, data])

def my_body(d):
    print("its " + str(d[1][d[0]]))

def my_condition(d):
    return d[0] < len(d[1])

while_loop([0, 1, 2, 9], my_condition, my_body)

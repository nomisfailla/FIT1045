def read_tides(filename):
    result = []
    with open(filename, "r") as file:
        for line in file:
            split = line.split(",")
            date = split[0]
            time = float(split[1])
            tide = float(split[2].split(' ')[0])

            result.append([date, time, tide])
    return result

def get_min_max(tide_data):
    res = []
    i = 0
    while i < len(tide_data):
        current_day = tide_data[i][0]
        tide_min = tide_data[i][2]
        min_time = tide_data[i][1]
        tide_max = tide_data[i][2]
        max_time = tide_data[i][1]
        while i <len(tide_data) and current_day == tide_data[i][0]:
            if tide_data[i][2] > tide_max:
                tide_max = tide_data[i][2]
                max_time = tide_data[i][1]
            if tide_data[i][2] < tide_min:
                tide_min = tide_data[i][2]
                min_time = tide_data[i][1]
            i += 1
        res.append([current_day, min_time, tide_min, max_time, tide_max])
    return res

def get_average_tides(tide_data):
    tide_data = get_min_max(tide_data)
    min_avg = 0
    max_avg = 0
    for day in tide_data:
        min_avg += day[1]
        max_avg += day[3]

    min_avg /= len(tide_data)
    max_avg /= len(tide_data)
    return (min_avg, max_avg)

data = read_tides("Tides.txt")
min_max = get_min_max(data)

for day in min_max:
    print(day)

avg_tides = get_average_tides(data)
print("Over the full period, on average the lowest and highest tides occured at " + str(avg_tides[0]) + " and " + str(avg_tides[1]) + " hours after midnight")

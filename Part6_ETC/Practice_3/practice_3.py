import csv


location = input("Input: ")

f = open('large_bike_1.csv', 'r')
rdr = csv.reader(f)

bike_log_by_location = []
for line in rdr:
    if line[12] == 'busan':
        bike_log_by_location_index = []
        bike_log_by_location_index.append(line[0].split()[0])
        bike_log_by_location_index.append(line[9])
        bike_log_by_location_index.append(line[10])
        bike_log_by_location.append(bike_log_by_location_index)
bike_log_by_location.sort(key=lambda x: x[0])

for line in bike_log_by_location:
    print(line[0]+": casual: "+line[1]+", registered: "+line[2])

f.close()

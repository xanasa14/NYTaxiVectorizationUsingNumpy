import numpy as np
import csv


# Listing the data from the csv file 
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))
# Getting rid of the header row
taxi_list = taxi_list[1:]


# Converting all the values into float 
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)


taxi = np.array(converted_taxi_list)
print (taxi)

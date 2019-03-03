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

# axis = 0 is for columns and axis = 1 is for rows
taxi_column_means = taxi.mean(axis=0)

#Sorting using Numpy
sorted_order = np.argsort(taxi[:,15])

taxi_sorted = taxi[sorted_order]

print(taxi_sorted)


#To read data from file and skip the header(first row) using Numpy
#taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)


#creating a copy of our taxi array
#taxi_modified = taxi.copy()
# changing values from the data that i just copied 
'''
Rows , Columns
taxi_modified[28214,5] = 1

taxi_modified[:,0] = 16
Here, i replaced these 2 values 1800 and 1801 by the mean of the column 
taxi_modified [1800:1802,7] = taxi_modified[:,7].mean()
'''

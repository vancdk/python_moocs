"""
How to read a csv file

"""

# Import module
import csv

# Import file
file = open("my_csv.csv")

# The reader() function of the CSV module will interpret the file as a CSV.
data = csv.reader(file)

# Unpack the data into named variables
for row in data:
  field_1, field_2, field_3 = row
  print("Field 1: {}, field 2: {}, field 3: {}".format(field_1, field_2, field_3))
  
# Close the file to save memory space
file.close()



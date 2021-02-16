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

"""
How to generate a csv file

"""

# Store the data that you want to write into a list of lists
hosts = [["workstation.local", "192.168.25.46"], [webserver.cloud", "10.2.6.5"]]

# Open the file with write permissions
with open('hosts.csv', 'w') as hosts_csv:
  # Create an instance of the writer Class
  writer = csv.writer(hosts_csv)
  writer.writerows(hosts)

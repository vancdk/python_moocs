
"""
Open modes are:
"r": open for reading (default)
"w": open for writing (!) The old contents get deleted as soon as we open the file (!)
"x": open for exclusive creation, failing if the file already exists
"a": open for writing, appending to the end of the file if it exists
"r+": open for updating (reading and writing)
"""

# Step 1
# Populate a file with each initial guest's first name on its own line.

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

with open("guests.txt") as guests:
    for line in guests:
      print(line)

# Step 2
# Add guests to the guests.txt file as they check in.

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)
        
# Step 3
# Remove the guests that have checked out already

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Step 4
# Check whether particular guests are still checked in.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

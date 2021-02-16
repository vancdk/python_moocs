"""
Files
"""
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")

"""
Directories
"""

# Get current directory
print(os.getdw())

# Create directory
os.mkdir("new_dir")

# Change the current working directory
os.chdir("new_dir")

# Remove an empty directory
os.mkdir("newer_dir")
os.rmdir("newer_dir")

# List all contents of a dir
os.listdir("downloads")

"""
Below is a snippet of code that displays the content
of the downloads directory along with the type of content

By using os.path.join we can concatenate directories 
in a way that can be used with other os.path() functions
in all operating systems.

"""

import os
dir = "downloads"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
	if os.path.isdir(fullname):
		print("{} is a directory".format(fullname))
	else:
		print("{} is a file".format(fullname))

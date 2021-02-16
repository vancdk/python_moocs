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


"""
Ways of iterating through the contents of a file.

If a file is very large, it's more memory efficient to process it line by line.
"""
# 1
file = open("my_file.txt")
# The readline() method reads a single line from the current position
lines = file.readlines()
file.close()
lines.sort()
print(lines)
"""
This will print:
 the lines sorted alphabetically
 "\n" for new line characters and "\t" for tabs
"""

# 2
# Python will automatically close the file at the end of a with block
with open("my_file.txt") as file:
  # The read() method reads until the end of the file, also from the current position
  print(file.read())
  
# 3
with open("my_file.txt") as file:
  for line in file:
    # Use strip() to avoid printing empty lines by eliminating the new line characters
    print(line.strip().upper())

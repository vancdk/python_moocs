
# Python will automatically close the file at the end of a with block
with open("my_file.txt") as file:
  # The readline() method reads a single line from the current position
  print(file.readline())
  # The read() method reads until the end of the file, also from the current position
  print(file.read())
  
 

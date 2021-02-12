
"""
Open modes are:
"r": open for reading (default)
"w": open for writing (!) The old contents get deleted as soon as we open the file (!)
"x": open for exclusive creation, failing if the file already exists
"a": open for writing, appending to the end of the file if it exists
"r+": open for updating (reading and writing)
"""

with open("my_novel.txt","w") as file:
  file.write("It was a warm and sunny day.")

# Tuples can contain elements of any data type, but unlike lists, they are immutable.
# They’re specified using parentheses instead of square brackets.
# Storing the elements of a tuple in separate variables is called unpacking. 
# This allows us to take multiple returned values from a function and store each value in its own variable.

# We can use tuples to store information about a file: its name, its type and its size in bytes. 
# file_size() returns the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 

def file_size(file_info):
	file_name, file_type, file_size = file_info
	return("{:.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21




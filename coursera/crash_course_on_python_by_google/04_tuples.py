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


# The skip_elements function returns every other element from the list
# It uses the enumerate function to check if an element is on an even position or an odd position.

def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

""" 
Tuples can contain elements of any data type, but unlike lists, they are immutable.
They’re specified using parentheses instead of square brackets.
  
  * Storing the elements of a tuple in separate variables is called unpacking. 
  This allows us to take multiple returned values from a function and store each value in its own variable.
  
  * The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. 
  The first value of the tuple is the index and the second value is the element itself. 
"""

# The file_size() function returns the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 

def file_size(file_info):
	file_name, file_type, file_size = file_info
	return("{:.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


# The skip_elements function returns every other element from the list

def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


# The octal_to_string function makes the code convert a permission in octal format into a string format.
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. 
# Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. 
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

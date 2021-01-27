# 1
# Print out the numbers 1 through 7.

number = 1
while number <= 7:
	print(number, end=" ")
	number += 1
  
  
# 2
# Print out each letter of a word on a separate line. 

def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")


# 3
# Returns how many digits the number has. 

def digits(n):
	count = 0
	if n == 0:
	  count = 1
	while not (n<1):
		count += 1
		n = n/10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1


# 4
# Print out a multiplication table (where each number is the result of 
# multiplying the first number of its row by the number at the top of its column).

def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)


# 5
# Count down from start to stop when start is bigger than stop, 
# and counts up from start to stop otherwise. 

def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


# 6
# Return a space-separated string of all positive numbers that are divisible by 2, 
# up to and including the maximum that's passed into the function. 

def even_numbers(maximum):
	return_string = ""
	for x in range(1, maximum+1):
		if x % 2 == 0:
		  return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed






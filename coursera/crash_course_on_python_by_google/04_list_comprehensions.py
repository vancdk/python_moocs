"""
List comprehensions allow you to create a new list from a sequence or a range in a single line.
"""

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 

def odd_numbers(n):
	return [x for x in range(1,n+1) if x%2==1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

# 1: is_power_of()

# Makes the is_power_of function return whether the number is a power of the given base.
# Note: base is assumed to be a positive number. 
# Remember: for functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# 2: sum_positive_numbers()

# A recursive function that returns the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  if n <= 1:
    return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

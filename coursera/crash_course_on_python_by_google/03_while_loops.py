# Makes the print_prime_factors function print all the prime factors of a number.
# Remember: a prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Starts with two, which is the first prime
  factor = 2
  # Keeps going until the factor is larger than the number
  while factor <= number:
    # Checks if factor is a divisor of number
    if number % factor == 0:
      # If it is, prints it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increments the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)

# Should print 2,2,5,5

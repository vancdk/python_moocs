# Make the factorial function return the factorial of n. 
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember: the factorial of a number is defined as the product of an integer and all integers before it.

def factorial(n):
  result = 1
  for x in range(1,n+1):
    result = result * x
  return result

for n in range(0,10):
  print(n, factorial(n))
  
# Result: 
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880

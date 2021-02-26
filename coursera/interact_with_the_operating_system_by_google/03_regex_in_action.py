import re

"""
By adding a ^ and a $ to the pattern, we only match 
strings that stricly begin and end with the pattern.

"""
print(re.search(r"A.*a", "Argentina"))
# match='Argentina'

print(re.search(r"A.*a", "Azerbaijan"))
# match='Azerbaija'

print(re.search(r"^A.*a$", "Azerbaijan"))
# None

print(re.search(r"^A.*a$", "Australia"))
# match='Australia'


"""
Let's construct a pattern that would validate if a string
is a valid variable name in Python.

*** starts with a letter
*** followed by as many numbers, letters or undescores as we want
*** ends there

"""
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name_1"))
# match='_this_is_a_valid_variable_name_1'

print(re.search(pattern, "this isn't a valid variable name"))
# None

print(re.search(pattern, "2_my_variable"))
# None

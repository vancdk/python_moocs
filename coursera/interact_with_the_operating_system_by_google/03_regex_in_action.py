import re

"""
Let's check, in a list of all the countries in the world,
which of those names start and end in A

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


"""
Let's construct a pattern that will check if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, 
and ends with a period, question mark, or exclamation point.

"""
pattern = r"^[A-Z][ |a-z]*[.?\!]$"

print(re.search(pattern, "is this is a sentence?"))
# None

print(re.search(pattern, "A star is born."))
# match='A star is born.'


"""
Extract PID from log message
"""

def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


"""
Regex expressions allow us to search a text for strings that match a certain pattern.

"""

import re

log = "July 31 04:50:43 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


# The r at the beginning indicates that this is a rawstring
result = re.search(r"aza", "plaza")
print(result)
# Prints: <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print(result)
# Prints: <re.Match object; span=(1, 4), match='aza'>

result = re.search(r"aza", "maze")
print(result)
# Prints: None

print(re.search(r"^x","xenon"))
# Prints: <re.Match object; span=(0, 1), match='x'>

print(re.search(r"p.ng","penguin"))
# Prints: <re.Match object; span=(0, 4), match='peng'>

print(re.search(r"p.ng","sponge"))
# Prints: <re.Match object; span=(1, 5), match='pong'>


# Additional options
print(re.search(r"p.ng","Pangaea", re.IGNORECASE))
# Prints: <re.Match object; span=(0, 4), match='Pang'>

print(re.search(r"[Pp]ython", "Python"))
# Prints: <re.Match object; span=(0, 6), match='Python'>

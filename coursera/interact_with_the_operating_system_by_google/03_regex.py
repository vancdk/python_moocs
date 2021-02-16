"""
Regex expressions allow us to search a text for strings that match a certain pattern.

"""

import re

log = "July 31 04:50:43 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


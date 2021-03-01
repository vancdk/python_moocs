import re


print(re.search(r"[a-zA-Z]{5}", "a ghost")) # match='ghost'
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) # match='scary'
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # ['scary', 'ghost', 'appea']

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")) # ['scary', 'ghost']

print(re.findall(r"\w{5,10}", "I really like strawberries")) # ['really', 'strawberri']

print(re.findall(r"\w{5,}", "I really like strawberries")) # ['really', 'strawberries']

print(re.search(r"s\w{,20}", "I really like strawberries")) # match='strawberries'


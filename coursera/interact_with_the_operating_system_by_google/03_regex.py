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
# <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(1, 4), match='aza'>

result = re.search(r"aza", "maze")
print(result)
# None

print(re.search(r"^x","xenon"))
# <re.Match object; span=(0, 1), match='x'>

print(re.search(r"p.ng","penguin"))
# <re.Match object; span=(0, 4), match='peng'>

print(re.search(r"p.ng","sponge"))
# <re.Match object; span=(1, 5), match='pong'>


# Additional options
print(re.search(r"p.ng","Pangaea", re.IGNORECASE))
# <re.Match object; span=(0, 4), match='Pang'>

print(re.search(r"[Pp]ython", "Python"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way"), "The end of the highway")
# <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go"))
# None
# Because the string "way" is preceded by a space

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0, 6), match='cloudy'>

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
# <re.Match object; span=(0, 6), match='cloud9'>

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# <re.Match object; span=(4, 5), match=' '>
# ^ excludes certain types of character

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# <re.Match object; span=(30, 31), match='.'>
# Because we added a space inside

print(re.search(r"cat|dog", "I like cats."))
# <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dog", "I like both dogs and cats."))
# <re.Match object; span=(7, 10), match='dog'>

print(re.findall(r"cat|dog", "I like both dogs and cats."))
['dog', 'cat']

"""
 Check if the text passed contains punctuation symbols: 
 commas, periods, colons, semicolons, question marks, and exclamation points.

"""

def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

"""
Repeated matches 
* 
+ matches 1 or more occurences of the character before it
? means either 0 or 1 occurence of the character before it

"""
print(re.search(r"Py.*n","Pygmalion"))
# Match Py followed by any number of characters followed by n
# <re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py.*n","Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>
# The stars takes as many characters as possible (it's greedy)

print(re.search(r"Py[a-z]*n","Pyn"))
# <re.Match object; span=(0, 3), match='Pyn'>

print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>
# There was 1 occurence of each pattern, the first one is returned

print(re.search(r"o+l+", "boil"))
# None
# Because it had another character in between them

print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like peaches"))
# <re.Match object; span=(7, 12), match='peach'>
# The "p" was present here, so the match included it


"""
The repeating_letter_a function checks if the text passed 
includes the letter "a" (lowercase or uppercase) at least twice.

"""

def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

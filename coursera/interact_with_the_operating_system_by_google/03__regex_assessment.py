import re

"""
The check_web_address function checks if the text passed qualifies as a top-level web address
meaning that it contains alphanumeric characters as well as periods, dashes, and a plus sign, 
followed by a period and a character-only top-level domain

"""
def check_web_address(text):
  pattern = r"^[\w\.-]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


"""
The check_time function checks for the time format of a 12-hour clock, as follows:
***  the hour is between 1 and 12, with no leading zero, followed by a colon, 
***  then minutes between 00 and 59,
***  then an optional space,
***  and then AM or PM, in upper or lower case. 

"""
def check_time(text):
  pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[AM|am|PM|pm]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


"""
The contains_acronym function checks the text for the presence of: 
***  2 or more characters or digits 
***  surrounded by parentheses, 
***  with at least the first character in uppercase (if it's a letter)

"""
def contains_acronym(text):
  pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


"""
The check_zip_code function checks if the text passed includes a possible U.S. zip code, formatted as follows:
***  exactly 5 digits, 
***  and sometimes, but not always, followed by a dash with 4 more digits.
"""

def check_zip_code (text):
  result = re.search(r"[ ]\d{5}[-]\d{4}|[ ]\d{5}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


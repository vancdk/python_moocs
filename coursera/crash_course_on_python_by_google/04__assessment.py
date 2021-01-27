# 1
# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: "house number X on street named Y".

def format_address(address_string):
  # Declare variables
  house_number = ""
  street_name = []
  street_name_string = ""

  # Separate the address string into parts
  address_split = address_string.split(' ')

  # Traverse through the address parts
  for address_part in address_split:
    # Determine if the address part is the
    # house number or part of the street name
    if address_part.isdigit():
      house_number = address_part
    else:
      street_name.append(address_part)

  # Does anything else need to be done 
  # before returning the result?
  house_number = str(house_number)
  street_name_string = " ".join(street_name)

  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name_string)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# 2
# The highlight_word function changes the given word in a sentence to its upper-case version. 

def highlight_word(sentence, word):
  return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# 3
#  Combine the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  new_list = []
  new_list = list2 + list1[::-1] 
  return new_list
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# 4
# Use a list comprehension to create a list of squared numbers (n*n)

def squares(start, end):
	return [ x**2 for x in range(start,end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 5
# Iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

def car_listing(car_prices):
  result = ""
  for car_name, car_price in car_prices.items():
    result += "{} costs {} dollars".format(car_name, car_price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# 6
# Combine both dictionaries into one, with each friend listed only once, 
# the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. 

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  all_guests = {}
  all_guests = guests2
  all_guests.update(guests1)
  return all_guests

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# 7 
# Use a dictionary to count the frequency of letters in the input string. 
# Only letters should be counted, not blank spaces, numbers, or punctuation. 
# Upper case should be considered the same as lower case. 

def count_letters(text):
  result = {}
  letters = text.strip().lower()
  # Go through each letter in the text
  for letter in letters:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
    # Add or increment the value in the dictionary
      if letter not in result:
        result[letter] = 1
      else:
        result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

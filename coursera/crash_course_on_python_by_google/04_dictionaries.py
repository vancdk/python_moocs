"""
Data in a dictionary is organized into pairs of keys and values. 
A dictionary key can be of almost any data type, like a string, integer, float, or even tuples.
"""

# The "toc" dictionary represents the table of contents for a book.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc)  # Is there a Chapter 5?


# Here we have a dictionary called "wardrobe" with items of clothing and their colors. 

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item_of_clothing in wardrobe.keys():
	for color in wardrobe[item_of_clothing]:
		print("{} {}".format(color, item_of_clothing))
    

# The groups_per_user returns a dictionary with the users as keys and a list of their groups as values. 

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			# groups for this user, creating the entry
			# in the dictionary if necessary
			if user in user_groups:
				user_groups[user].append(groups)
			else:
				user_groups[user] = []
				user_groups[user].append(groups)

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

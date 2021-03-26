#!/usr/bin/env python3

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True


"""
# Before assertion: 

>>> validate_user("",-2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in validate_user
ValueError: minlen must be at least 1
>>> validate_user("",1)
False
>>> validate_user("myuser",1)
True
>>> validate_user(88,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in validate_user
TypeError: object of type 'int' has no len()
>>> validate_user([],1)
False
>>> validate_user(["name"],1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in validate_user
AttributeError: 'list' object has no attribute 'isalnum'

# After assertion

>>> validate_user([2], 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in validate_user
AssertionError: username must be a string

"""

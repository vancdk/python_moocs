"""
Objects are an encapsulation of variables and functions into a single entity.
Calling methods on objects executes functions that operate on attributes of a specific instance of the class.
When you have variables that contain different values for different instances, these are called instance variables.
"""

# In this code, there's a Person class that has an attribute name, which gets set when constructing the object. 

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Sam") 
# Call the greeting method
print(some_person.greeting())


# In addition to the __init__ constructor special method, there is also the __str__ special method. 
# It defines how an instance of an object will be printed when it’s passed to the print() function.

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


# A docstring is a short text explanation of what something does. 

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

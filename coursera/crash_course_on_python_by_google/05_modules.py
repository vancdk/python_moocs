# Let's take a look at the datetime module. 
# First, we import the module. Next, we call the now() method which belongs to the datetime class contained within the datetime module.

import datetime
now = datetime.datetime.now()
type(now)
# prints <class 'datetime.datetime'>
print(now)
# prints 2019-04-24 16:54:55.155199
now.year
# prints 2019


# We can access other classes contained in the datetime module, like the timedelta class.
# We’re then adding this object to our instance of the datetime class from earlier and printing the result. 

print(now + datetime.timedelta(days=28))
# prints 2019-05-22 16:54:55.155199

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in event.machine:
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
      
"""
No output should be generated from running the custom function definitions above. 
To check that our code is doing everything it's supposed to do, we need an Event class. 
The code in the next cell below initializes our Event class.

"""

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user
    
    
# Next let's create some events and add them to a list.

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]


# Let's feed these events into our custom_users function and see what happens.

users = current_users(events)
print(users)

# Should print: {'webserver.local': {'lane', 'jordan'}, 'myworkstation.local': {'jordan'}, 'mailserver.local': set()}

generate_report(users)

"""
Should print: 
webserver.local: lane, jordan
myworkstation.local: jordan

"""

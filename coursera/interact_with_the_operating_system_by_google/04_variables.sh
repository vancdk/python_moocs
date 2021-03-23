# Environment variables

$ cat variables.py
#!/usr/bin/env python3

import os

print("HOME: "+os.environ.get("HOME", ""))
print("SHELL :"+os.environ.get("SHELL", ""))
print("FRUIT: "+os.environ.get("FRUIT", ""))

$ chmod +x variables.py

$ ./variables.py
HOME: /Users/vancdk
SHELL :/bin/bash
FRUIT: 

$ export FRUIT=Pinapple
$ ./variables.py
HOME: /Users/vancdk
SHELL :/bin/bash
FRUIT: Pinapple

# Command-Line Arguments 
$ cat parameters.py

$ chmod +x ./parameters.py
#!/usr/bin/env python3

import sys
print(sys.argv)

$ ./parameters.py one two three
['./parameters.py', 'one', 'two', 'three'] # The list of arguments are stored in the sys module.

# Exit Status
$ wc variables.py 
       8      13     169 variables.py

$ echo $?
0

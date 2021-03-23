$ cat variables.py
#!/usr/bin/env python3

import os

print("HOME: "+os.environ.get("HOME", ""))
print("SHELL :"+os.environ.get("SHELL", ""))
print("FRUIT: "+os.environ.get("FRUIT", ""))

$ chmod +x variables.py

$ ./variables.py
HOME: /Users/vanessachaddouk
SHELL :/bin/bash
FRUIT: 

$ export FRUIT=Pinapple
$ ./variables.py
HOME: /Users/vanessachaddouk
SHELL :/bin/bash
FRUIT: Pinapple

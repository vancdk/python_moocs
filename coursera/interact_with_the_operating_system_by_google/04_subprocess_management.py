# Calling the copy method of the os.environ dictionary will copy the current environment variables 
# to store and prepare a new environment by creating a new dictionary of environment variables.

# Link to official documentation: https://docs.python.org/3/library/subprocess.html

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/example_app/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)


# Running a child process and obtaining the exit status 

>>> import subprocess
>>> subprocess.run(["date"])
Mar 23 mar 2021 15:08:08 CET
CompletedProcess(args=['date'], returncode=0)
>>> subprocess.run(["sleep","2"])
CompletedProcess(args=['sleep', '2'], returncode=0)
>>> result = subprocess.run(["ls", "this_file_doesnt_exist"])
ls: this_file_doesnt_exist: No such file or directory
>>> print(result.returncode)
1

# Obtaining the output of a system command
>>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
>>> print(result.returncode)
0
>>> print(result.stdout)
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n' # 'b' means it's an array of bytes
>>> print(result.stdout.decode().split())
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

>>> result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
>>> print(result.returncode)
1
>>> print(result.stdout)
b''
>>> print(result.stderr)
b'rm: does_not_exist: No such file or directory\n'

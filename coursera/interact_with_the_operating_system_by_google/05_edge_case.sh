$ ./rearrange_test.py 
.E
======================================================================
ERROR: test_empty (__main__.TestRearrange)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./rearrange_test.py", line 14, in test_empty
    self.assertEqual(rearrange_name(testcase), expected)
  File "/Users/vanessachaddouk/rearrange.py", line 7, in rearrange_name
    return "{} {}".format(result[2], result[1])
TypeError: 'NoneType' object is not subscriptable

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (errors=1)


$ cat rearrange.py
#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result is None:
    return ""
  return "{} {}".format(result[2], result[1])
  
$ ./rearrange_test.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

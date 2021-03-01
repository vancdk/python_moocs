import re

def rearrange_name(name):
  result = re.search(r"^([\w \.]*), ([\w \.]*)$", name)
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

rearrange_name("Ritchie, Dennis") # 'Dennis Ritchie'
rearrange_name("Hopper, Grace M.") # 'Grace M. Hopper'

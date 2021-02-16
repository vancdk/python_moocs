"""
This is an executable script that does two health checks.
First, a check_disk_usage() function that recieves a distant check and returns TRUE if it's
more than 20% free or FALSE if it's less.
Second, a check_cpu_usage() function that checks the usage for a whole second and returns TRUE
if the CPU usage is less than 75%.

If either of these two functions returns FALSE, the script prints an error.

"""

#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
  """Verifies that there's enough free space on disk"""
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def check_cpu_usage():
  """Verifies that there's enough unused CPU"""
  usage = psutil.cpu_percent(1)
  return usage < 75

# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage("/") or not check_cpu_usage():
  print("ERROR!")
else:
  print("OK.")

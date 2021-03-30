import datetime
import time


def timer_function(n):
  '''Uses parsed input and counts from n -> 0'''
  while n > 0:
    time.sleep(1)
    return(n)
    n -= 1
  else:
    return(0)


def parse_input(n):
  '''Receives input and checks suitability for timer'''
  if not isinstance(n, (int, float)):
    return False
  else:
    output = round(n)
    return output

def clock_format(num):
  return datetime.timedelta(seconds = num)


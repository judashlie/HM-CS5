# python 2
#
# Homework 2, Problem 2
#
# Name: JLM
# Date: 06.28.2016
#

def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x
    
def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x
    
def sq(x):
  """ output: square of input
      input x: a number (int or float)
  """
  return x*x
  
def interp(low, hi, fraction):
  """ input: 3 numbers (float)
      output: fraction point b/n hi and low
              unless 0 or 1
  """
  return ((hi - low)*fraction) + low
  
def checkends(s):
  """ output: True if first & last chars match, else False
      input: string
  """
  if s[0] == s[-1] :
    return True
  else:
    return False
    
def flipside(s):
    """ input: string
        output: first half and second half of string flipped
    """
    x = len(s)/2
    return s[(x):]+ s[:x]
    
def convertFromSeconds(s):
  """ input: number of seconds (int)
      output: (int) list of equiv days, hours, minutes, seconds
  """
  days = s / (24*60*60)  # # of days
  s1 = s % (24*60*60)     # the leftover
  hours = s1 / (60*60) # # of hours
  s2 = s1 % (60*60)
  minutes = s2 / 60
  s3 = s2 % 60
  seconds = s3
  return [days, hours, minutes, seconds]
    
def front3(str):
  """ input: string
      output: first 3 chars, rptd 3x
  """
  f3 = str[:3]
  return f3+f3+f3

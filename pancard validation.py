#Write a program to check pancard validation
"""should have exactly 10 characters the first 5 characters
should be upper case, the next 4 should be numbers, and last one
should be an upper case character"""

import re
pancard = input()
if(re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pancard)):
   print("Valid")
else:
   print("Invalid")
   

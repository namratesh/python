#Write a program to check email validation
import re
email = input()
if(re.match(r'^[A-Za-z][@]$', email)):
   print("Valid")
else:
   print("Invalid")
#Python program to toggle each character in a string
str = "python Is a ProgRAmminG Language"


for i in str:
    if i.isupper():
        print( i.lower(),sep='',end='')
    else:
        print( i.upper(),sep='',end='')

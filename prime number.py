#Check a number is prime or not.
"""A prime number is a whole number greater than 1
whose only factors are 1 and itself."""
num = int(input("Enter a number: "))
if(num>2):
    for i in range(2,num):
       if(num%i==0):
           print(num , " is not a prime number")
           break
    else:
            
        print(num, " is a prime number")

else:
     print(num , " is not a prime number")

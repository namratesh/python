#find a reverse factorial of a given number
import sys
n = int(input())
temp=1
for i in range(2,n+1):
    fact = i*temp;
    temp = fact
    if(temp==n):
       print(i)
       sys.exit()
print("Given number is not a factorial of any number")
        
    
    

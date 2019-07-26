#find a factorial of a given number
n = int(input())
temp = 1
for i in range(2,n+1):
    fact = i*temp;
    temp = fact
    
print(fact)
        
    
    

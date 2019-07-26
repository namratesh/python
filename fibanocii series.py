#Write a program to find Fibonacci series up to n

def fibanoci(n):
     if n <= 1:  
       return n  
     else:  
       return(fibanoci(n-1) + fibanoci(n-2))

print(fibanoci(2))
print(fibanoci(11))
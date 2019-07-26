#print a prime number in a given range
start = int(input("Enter the first number:"))
end = int(input("Enter the last number:"))
for i in range(start,end):
    if(i>1):
        for j in range(2,i):
           if(i%j)==0:
              break
        else:
            print(i)
          

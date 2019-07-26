#write a program to find factor of given number
num = int(input("Enter a number: "))
print("factors of {} are ".format(num))
for i in range(1,num):
    if(num%i==0):
        print(i, end = ' ')
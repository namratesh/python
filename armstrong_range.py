#Print Armstrong number in a given range.
"""
 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
"""
first_num = int(input("Enter a first number: "))
last_num = int(input("Enter a last number: "))
for num in range(first_num,last_num):
    sum = 0  
    temp = num  
      
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
    if sum==num:
        print(num)

#check a number is palindrome or not
"""A number is said to be palindrome
if it is equals to it reverse."""

num = int(input())
temp = num
rev = 0
while temp!=0:
    rev = (rev*10)+(temp%10)
    temp = temp//10
if num == rev:
    print("number is palindrome")
else:
    print("number is not palindorme")

#Write a program to convert  Celsius to Farenheit.
"""Hint : 5 * (F – 32) = 9 * C,  F-Farenheit , C- Celsius"""
print("choose: \n1.celsius to farenhiet \n2.farenhiet to celcius")
n = int(input())

if(n==1):
    C = int(input("Enter a temperature in celcius: "))
    F = (9*C+160)/5 +"f"
    print("{} degree celcius in farenhiet is {}" .format(C,F))
    
elif(n==2):
    F = int(input("Enter a temperature in farenhiet: "))
    C = (5*F-160)/9
    print("{} degree farenhiet in celcius is {}" .format(F,C))
    

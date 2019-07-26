#find a lcm of two given number
a,b = 3,4
if a>b:
    greater = a
else:
    greater = b
while(True):
    if((greater % a == 0) and (greater % b == 0)):
        lcm = greater
        break
    greater+=1
    
print(lcm)
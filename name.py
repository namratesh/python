subject=[]
number=[]
failsubject=[]
numberii=[]
name=input( "Name = ")
c= int (input("Class = "))
rollno=input("Roll Number = ")
p=int(input("how many subject = "))
for i in range( 0,p):
    sub = input("Subjct name = ")
    m=int(input( "number = "))
    if (m<=33):
        failsubject.append(sub)
        numberii.append(m)
    else:
        subject.append(sub)
        number.append(m)
dic_pass=dict(zip(subject,number))
dic_fail=dict(zip(failsubject,numberii))
k=0
for num in  (number):
    num=num+k
    k=num
temp=0
for add in (numberii):
    add=add+temp
    temp=add
totalnumber= k+temp
print("Name = ",name)
print("Class = ",c)
print("Roll Number = " ,rollno)
print("pass subjec = ",dic_pass)
print("fail subject = ",dic_fail)
print("total number = ",totalnumber)
d= p*100
percent=(totalnumber/d)*100
print("percent =",percent)
if (len(dic_fail)>0):
    print("Result = fail")
else:
    if(percent>60):
        print("pass in first division")
    elif(percent>40 and percent<60):
        print("pass in second divison")
    elif(percent>33 and percent<40):
        print("pass")
    

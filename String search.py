"""write a program to take n number of courses as input and
to check particular course available or not"""
n = int(input("Enter number of courses: "))
l = []
print("Enter the courses :")
for i in range(0,n):
    string = str(input())
    l.append(string)
search_course = str(input("Enter a course to be searched: "))
if search_course in l:
    print("yes, course exist")
else:
    print("No, course doesn't exist")
    
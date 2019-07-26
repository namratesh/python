#Write a program to find and replace a string
string = "python is created by Guido ven Rossum"
search = str(input("Enter a string to search: "))
rep = str(input("Enter a string to replace: "))
if search in string:
    new_string = string.replace(search,rep)
    print(new_string)
else:
    print("string is not available")
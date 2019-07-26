#check a String is palindrome or not
"""A String is said to be palindrome
which read same forward and backword."""

Str = input()
rev = reversed(Str)
if list(Str)== list(rev):
    print("String is palindrome")
else:
    print("String is not palindorme")

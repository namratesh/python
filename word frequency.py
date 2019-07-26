#Program to calculate the Frequency of characters in a string

str = "programming is love"

"""method -1"""
res = {}   
for keys in str: 
    res[keys] = res.get(keys, 0) + 1
print(res)

"""method -2"""
from collections import Counter
print(Counter(str)) 
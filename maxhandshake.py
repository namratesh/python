#Find the maximum number of handshakes
"""There are N persons in a room. Find the maximum number of Handshakes possible.
Given the fact that any two persons shake hand exactly once."""

n = 12 #no of people
maxHandshake = n*(n-1)//2
print(maxHandshake)

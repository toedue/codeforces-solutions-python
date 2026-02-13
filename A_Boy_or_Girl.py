from collections import Counter 

username = input()

d = Counter (username)

length = len(d)

if length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

# print(d, length)

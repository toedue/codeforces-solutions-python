n = int(input())
s = input()

a, d = 0, 0
for char in s:
    if char == "A":
        a += 1
    else:
        d += 1
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
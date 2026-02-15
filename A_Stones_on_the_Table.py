n = int(input())
s = input()

str = []
counter = 0
for i in range (1,len(s)):
    if s[i-1] == s[i]:
        counter += 1
print(counter)
s = input()

n = int(input())

arr = []
for _ in range(n):
    l, r = map(int, input().split())
    arr.append((l,r))

ps = [0] * (len(s) + 1)

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        ps[i] = 1

for i in range(1,len(ps)):
    ps[i] += ps[i-1]

        
# print(ps)

for l , r in arr:
    print(ps[r-1] - ps[l-1])


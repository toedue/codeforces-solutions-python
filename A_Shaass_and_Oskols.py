n = int(input())

birds = list(map(int, input().split()))

m = int(input())
arr = []
for i in range(m):
    x,y = map(int, input().split())
    arr.append((x,y))

d = {k+1:v for k,v in enumerate(birds)}


for i,j in arr:

    if i-1 in d:
        d[i-1] += (j-1)
    if i + 1 in d:
        d[i+1] += d[i]-j

    d[i] = 0

for val in d.values():
    print(val)

        
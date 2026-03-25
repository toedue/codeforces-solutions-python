k = int(input())
r = list(map(int, input().split()))

r.sort()

# print(r)

x = r[-1]

print(max(0,x-25))
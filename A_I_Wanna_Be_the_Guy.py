n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))


combined = set(x[1:]+y[1:])

print("I become the guy.") if len(combined) == n else print("Oh, my keyboard!")
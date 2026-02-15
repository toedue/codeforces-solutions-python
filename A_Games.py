n = int(input())
home = []
away = {}
counter = 0

for _ in range(n):
    h, a = input().split()
    home.append(h)
    away[a] = away.get(a,0) + 1

for h in home:
    counter += away.get(h, 0)
    
print(counter)


a, b = map(int, input().split())

path = []

while b > a:
    path.append(b)
    
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break

# Check if we reached a
if b == a:
    path.append(a)
    path.reverse()
    
    print("YES")
    print(len(path))
    print(*path)
else:
    print("NO")
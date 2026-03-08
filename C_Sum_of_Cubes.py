t = int(input())

for _ in range(t):
    x = int(input())
    found = False
    
    for a in range(1, 10001):
        a3 = a*a*a
        
        if a3 > x:
            break
        
        b3 = x - a3
        
        b = round(b3 ** (1/3))
        
        if b > 0 and b*b*b == b3:
            found = True
            break
    
    if found:
        print("YES")
    else:
        print("NO")
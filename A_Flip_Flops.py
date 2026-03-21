t = int(input())

for _ in range(t):
    n, c, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    for i in range(n):
        if a[i] > c:
            break
        
        increase = min(k, c - a[i])
        a[i] += increase
        k -= increase
        c += a[i]
    
    print(c)

n = int(input())
r=0
while (n >0):
    p,q = list(map(int,input().split()))
    
    if (p+2 <= q):
        r+=1
    n-=1
print(r)
n = int(input())
for i in range(n):
    print(" "*(n*2)+str(i)+" "*(n*2))
    n-=2
for i in range(n+1):
    print(" "*(n*2)+str(n-i)+" "*(n*2))




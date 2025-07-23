t = int(input())
for i in range (t):
    m,a,b,c = map(int,input().split())
    seats=0
    lseats=0
    if m >= a:
        seats += a
        lseats += (m-a)
    else:
        seats+=m
    
    if m >= b:
        seats += b
        lseats += (m-b)
    else:
        seats+=m

    if (m>0):
        seats += min(c,lseats)
    print(seats)

       
    

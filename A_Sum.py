t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    big = max (a,b,c)    
    sum = a+b+c
    sum_of_two = sum - big

    if sum_of_two == big:
        print("YES")
    else:
        print("NO")
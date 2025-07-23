t = int (input())
for i in range (t):
    n,k = map(int, input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))


    a_withindex = [(a[i],i) for i in range(n)]

    a_withindexS = sorted(a_withindex)
    b_sorted = sorted(b)

    result = [0]*n

    for i in range (n):
        result[a_withindexS[i][1]] = b_sorted[i]

    print (' '.join(map(str,result)))

        

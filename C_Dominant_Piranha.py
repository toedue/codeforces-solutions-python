t = int(input())

for _ in range(t):
    n = int(input())

    pir = list(map(int, input().split()))

    if n <= 1:
        print(-1)
        continue
    
    mx= max(pir)
    flag = False

    for i in range(n):
        if pir[i] == mx:
            if i > 0 and pir[i-1] < mx:
                flag = True
                break
            if i< n - 1 and pir[i+1] < mx:
                flag = True
                break

    if flag:
        print(i + 1)
    else:
        print(-1)



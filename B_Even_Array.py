t = int(input())

for i in range(t):
    ecounter = 0
    ocounter = 0
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        if (i%2) != (arr[i]%2):
            if arr[i]%2 == 0:
                ecounter+=1
            else:
                ocounter +=1

    if ecounter == ocounter:
        print(ecounter)
    else:
        print(-1)




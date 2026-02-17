test_case = int(input())



for _ in range(test_case):
    m, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    found = set(arr)

    i = 1

    while s > 0:
        if i not in found:
            s -= i
            arr.append(i)

        i +=1

    if s == 0 and len(arr) == max(arr):
        print("YES")

    else:
        print("NO")


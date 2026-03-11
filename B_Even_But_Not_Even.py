t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    nums = list(map(int,s))
    ps = [x for x in nums]

    for i in range(1,n):
        ps[i] += ps[i-1]

    # print(ps)

    right = n-1
    res = ""

    while (right):
        if ps[right] % 2 == 0 and nums[right] % 2 != 0:
            res = "".join(map(str,nums[:right+1]))
            break
        else:
            right -= 1

    if res:
        print(res)
    else:
        print(-1)

    







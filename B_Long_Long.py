testCase = int(input())
for i in range(testCase):
    length = int(input())
    nums = list(map(int, input().split()))
    
    operation  = 0
    i = 0
    while (i < length):
        if nums[i] < 0:
            operation += 1
            while(i < length and nums[i] <= 0):
                i += 1

        else:#if num is 0 or positive
            i += 1

    total = sum(map(lambda x: abs(x), nums))

    print(f"{total} {operation}")
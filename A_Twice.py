t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    counter =0
    for i in range(1, n):
        if nums[i-1] == nums[i]:
            counter += 1
    print(counter)

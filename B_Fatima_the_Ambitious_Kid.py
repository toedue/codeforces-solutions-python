n = int(input())
nums = list(map(int,input().split()))

zero = False
for i in nums:
    if i == 0:
        zero = True
        break
    
if zero:
    print(0)
else:
    minimum = abs( nums[0])  

    for num in nums:
        temp = abs(num)

        if temp <  minimum:
             minimum = temp
    print(minimum)

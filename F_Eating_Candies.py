"""
6
2 1 4 2 4 1
l         r
"""

testCases = int(input())
for _ in range(testCases):
    size = int(input())
    candies = list(map(int, input().split()))
    # print(candies)
    l =0
    r = size -1
    sumL = 0
    sumR = 0
    result = 0
    while l <= r: # 0<=5,1<=5, 1<=4, 1<=3, 2<=3, 3<=3
        if sumL < sumR: # 2<5, 3<5
            sumL += candies[l] # sumL=3, sumL=7
            l += 1             # 2, 3
        elif sumL > sumR: # 2>0, 2>1, 7>5
            sumR += candies[r]  # sumR=1, sumR=5, sumR=7
            r -= 1               #4, 3, 2
        if sumL == sumR: # 0==0, 7==7
            result = max(result, l + (size - 1 - r)) # max(0,0), max(0, 3 + (6-1-2))
            sumL += candies[l]  #  sumL=2
            l +=1              # l=1
            

    print(result)
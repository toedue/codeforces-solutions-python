test_case = int(input())

for _ in range(test_case):
    
    n = int(input())

    prices = list(map(int, input().split()))

    ptr1 = n -1
    ptr2 = n-2
    bad = 0

    if n == 1:
        print(0)
        continue

    while(ptr2 >= 0):
        if prices[ptr2] > prices[ptr1]:
            bad += 1
            ptr2 -= 1
        elif prices[ptr2] < prices[ptr1]:
            ptr1 = ptr2
            ptr2 -=1
        else:         
            ptr2 -= 1

    print(bad)
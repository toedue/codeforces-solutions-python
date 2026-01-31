testCase = int(input())
for i in range(testCase):
    num = int(input())
    result = []
    multiplier = 1
    while num > 0:
        # get the last digit
        digit = num % 10
        if digit != 0:
            result.append(digit*multiplier)
            
        multiplier *= 10
        # updating num
        num //= 10
    
    print(len(result))
    #unpacking
    print(*result)
            
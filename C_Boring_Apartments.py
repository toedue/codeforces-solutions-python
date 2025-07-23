t = int(input())

for i in range(t):
    x = input()
    sum = 0
    for i in range(len(x)+1):
        sum += i
    print((int(x[0])*10)- 10 + sum)
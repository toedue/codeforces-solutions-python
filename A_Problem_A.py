n = int(input())
arr = list(map(int,input().split()))

sereja_score = 0
dima_score = 0

pointer1= 0
pointer2 = n-1

move = 0

while (pointer1 <= pointer2):
    if arr[pointer1] >= arr[pointer2]:
        big = arr[pointer1]
        pointer1 +=1

    else:
        big = arr[pointer2]
        pointer2 -=1

    if move %2 == 0:
        sereja_score += big
    else:
        dima_score += big

    move+=1

print (sereja_score, dima_score)


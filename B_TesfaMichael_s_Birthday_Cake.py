n, k = map(int, input().split())

s = input()

s = sorted(s)

# print(s)

total = 0
last = float('inf')
count =0


for c in s:
    if count == 0:
        last = ord(c) 
        total += ord(c) - ord('a') + 1
        count += 1

    else:
        if ord(c)- last >=2:
            last = ord(c)
            total +=  ord(c) - ord('a') + 1
            count += 1

    if count == k:
        break


if count == k:
    print(total)
else:
    print(-1)



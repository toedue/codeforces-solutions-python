n = int(input())

events = list(map(int, input().split()))

police = 0
crime = 0

for num in events:
    if num >= 1:
        police += num

    elif num < 0 and police == 0:
        crime += 1
    elif num < 0 and police >= 1:
        police += num

print(crime)


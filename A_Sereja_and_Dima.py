n = int(input())

cards = list(map(int, input().split()))

left = 0
right = n -1

sereja = 0
dima = 0

turn = 1
while(left <= right):
    if turn % 2== 1 and cards[left] >= cards[right]:
        sereja += cards[left]
        left += 1
    elif turn % 2== 1 and cards[left] <= cards[right]:
        sereja += cards[right]
        right -= 1
    elif turn % 2== 0 and cards[left] >= cards[right]:
        dima += cards[left]
        left += 1
    elif turn % 2== 0 and cards[left] <= cards[right]:
        dima += cards[right]
        right -= 1
    turn += 1

print(sereja, dima)


t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())

    deck = list(map(int, input().split()))

    current = 0
    ans = 0
    left = 0

    for right in range(n):
        current += deck[right]

        # if the sum is too big, remove cards from the left
        while current > r and left <= right:
            current -= deck[left]
            left += 1

        if current >= l and current <= r:
            ans += 1
            current = 0
            left = right + 1
    print(ans)

        

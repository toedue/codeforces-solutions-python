n, t = map(int, input().split())

books = list(map(int, input().split()))

count = 0
sum = 0
l = 0

for r in range(len(books)):
    sum += books[r]
    while l < n and sum > t:
        sum -= books[l]
        l += 1
    
    count = max(count, r-l + 1)


print(count)


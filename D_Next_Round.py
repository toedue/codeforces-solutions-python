n , k = map(int, input().split())

participant = list(map(int, input().split()))

counter = 0
for i in range(n):
    if participant[i] > 0 and participant[i] >= participant[k-1]:
        counter += 1
print (counter)

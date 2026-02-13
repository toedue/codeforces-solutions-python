n = int(input())

magnets = list(input() for _ in range(n))

counter = 1

for i in range(1, len(magnets)):
    if magnets[i-1] != magnets[i]:
        counter += 1
print(counter)
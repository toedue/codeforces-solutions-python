n, k = map(int, input().split())

instruments = list(map(int, input().split()))

arr = []

for idx, val in enumerate(instruments):

    arr.append((val, idx + 1))

arr.sort()

total_days = 0
indices = []
max_ins = 0

for day, idx in arr:

    if total_days + day <= k:
        total_days += day
        indices.append(idx)
        max_ins  += 1
    else:
        break
print(max_ins )
print(*indices)

n = int( input())

stones = list(map(int, input().split()))

m = int(input())

questions = []
for _ in range(m):
    type, l, r = map(int, input().split())
    questions.append((type, l, r))

stones_ps = [0] + stones[:]
# print(stones_ps)

for i in range(1,len(stones_ps)):
    stones_ps[i] += stones_ps[i-1]

# print(stones_ps)

stones.sort()
sorted_stones_ps = [0] + stones

# print(sorted_stones_ps)

for i in range(1,len(sorted_stones_ps)):
    sorted_stones_ps[i] += sorted_stones_ps[i-1]

# print(sorted_stones_ps)

for t, l, r in questions:
    if t == 1:
        print(stones_ps[r] - stones_ps[l-1])
    else:
        print(sorted_stones_ps[r] - sorted_stones_ps[l-1])






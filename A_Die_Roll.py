y, w = map(int, input().split())

point = max(y,w)

a = (6 - point) + 1

prob = { 1: "1/6", 2: "1/3", 3: "1/2", 4: "2/3", 5: "5/6", 6: "1/1"}

print(prob[a])
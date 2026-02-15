a1, a2, a3, a4 = map(int, input().split())

s = input()

d = {"1":a1, "2":a2, "3":a3, "4":a4}

total_calories = 0

for char in s:
    total_calories += d[char]

print(total_calories)
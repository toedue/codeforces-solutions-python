n = int(input())
solved_problem = 0
for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        solved_problem += 1

print(solved_problem)


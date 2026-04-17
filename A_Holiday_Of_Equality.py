n = int(input())

a = list(map(int, input().split()))

max_welfare = max(a)
total_spent = 0

for ai in a:
    total_spent += (max_welfare - ai)

print(total_spent)


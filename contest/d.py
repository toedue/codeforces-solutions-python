def solve():
    s = input()
    zero = s.count("0")
    one = s.count("1")
    if zero < one:
        print(zero)
    elif zero > one:
        print(one)
    else:
        print(0)

t = int(input())
for _ in range(t):
    solve()

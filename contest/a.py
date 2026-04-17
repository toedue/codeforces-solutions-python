def solve():
    d,t = map(int,input().split())

    if d <= t:
        print(0)
        return
    counter = 1

    while d / 2 > t:
        d = d/2
        counter +=1
    print(counter)



t = int(input())
for _ in range(t):
    solve()
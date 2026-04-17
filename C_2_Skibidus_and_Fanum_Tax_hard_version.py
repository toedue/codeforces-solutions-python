import bisect

def solve():
    n , m = map(int, input().split())

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    b.sort()
    prev = float("-inf")
    possible = True


    for ai in a:
        best = None

        #option 1
        if ai >= prev:
            best = ai

        # option 2
        target = prev + ai

        index = bisect.bisect_left(b, target)

        if index < m:
            new_val = b[index] - ai

            if best is None or new_val < best:
                best = new_val
        if best is None:
            possible = False
            break

        prev = best

    if possible:
        print("YES")
    else:
        print("NO")

t = int(input())

for _ in range(t):
    solve()


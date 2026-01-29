testCase = int(input())
for i in range(testCase):
    a, b, c, d = map(int, input().split())

    if (a == b == c == d):
        print("YES")
    else:
        print("NO")


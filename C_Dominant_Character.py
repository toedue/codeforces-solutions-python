t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = -1
    found = False

    for i in range(n-1):
        sub = s[i:i+2]
        if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
            ans = 2
            found = True
            break

    if not found:
        for i in range(n-2):
            sub = s[i:i + 3]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                found = True
                ans = 3
                break

    if not found:
        for i in range(n-3):
            sub = s[i:i + 4]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                found = True
                ans = 4
                break

    if not found:
        for i in range(n-6):
            sub = s[i:i + 7]
            if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                found = True
                ans = 7
                break
    print(ans)

    
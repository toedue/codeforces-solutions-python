t = int(input())

for _ in range(t):
    n = int(input())

    s = input()

    moves = 0
    stack = []

    for c in s:
        if c =="(":
            stack.append(c)

        else:
            if stack:
                stack.pop()
            else:
                moves += 1
    print(moves)
        
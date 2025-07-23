t = int(input())
for i in range(t):
    s = input()
    if len(s) == 2:
        print("i")
    else:
        print(s[:len(s)-2]+'i')
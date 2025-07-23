t = int(input())
for i in range(t):
    a = input()
    reversed = a[::-1]
    rl = list(reversed)
    for j in range(len(rl)):
        if rl[j] == "q":
            rl[j]="p"
        elif rl[j] == "p":
            rl[j]="q"
            
    print("".join(rl))
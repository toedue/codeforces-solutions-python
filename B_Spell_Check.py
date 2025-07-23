t = int(input())
Timur = "Timur"
target = sorted(Timur)
for i in range(t):
    n = int(input())
    str = input()
    
    if n == 5:
        if sorted(str) == target:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
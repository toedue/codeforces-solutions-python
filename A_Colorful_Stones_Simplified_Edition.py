s = input()
t = input()

ptr = 0


for i in range(len(t)):
    if ptr < len(s) and t[i] == s[ptr]:
        ptr += 1
        
print(ptr + 1)
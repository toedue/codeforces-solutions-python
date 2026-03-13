s = input()
s = s.lower()
ans = []

for c in s:
    if c not in "aeyoui":
        ans.append(f".{c}")

print("".join(ans))




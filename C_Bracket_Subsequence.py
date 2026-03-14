n , k = map(int, input().split())

s = input()

open_needed = k/2
close_needed = k/2
open_used = 0 
close_used = 0

ans = []

for c in s:
    if c == '(' and open_used < open_needed:
        ans.append(c)
        open_used += 1
    if c ==')' and close_used < close_needed and close_used < open_needed:
        ans.append(c)
        close_used += 1

    if len(ans) == k:
        break

print("".join(ans))
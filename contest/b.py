def solve():
    s = list(input())
    deleted = 0
    found = False
    left = 0
    right = 0

    while right < len(s):
        found = False
        counting = dict()
        curr = 0
        while not found and right < len(s):
            counting[s[right]] = counting.get(s[right],0) + 1
            curr += 1
            for key, val in counting.items():
                if val == 2:
                    deleted += curr - val
                    left = right + 1
                    found = True
            
            right += 1

        if right == len(s) and not found:
            deleted += curr
        

            right += 1
    print(deleted)
                

t = int(input())
for _ in range(t):
    solve()







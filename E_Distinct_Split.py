from collections import Counter
from collections import defaultdict

test_case = int(input())

for i in range(test_case):
    max_split = 0
    n = int(input())
    string = input()

    left = defaultdict(int)
    right  = Counter(string)

    for char in string:
        left[char] +=1
        right[char] -= 1

        if right[char] == 0:
            del right[char]
        max_split = max(max_split, len(right) + len(left))

    print( max_split)
        


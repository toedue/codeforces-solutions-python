from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    size = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue 

    freq = defaultdict(list)

    for i in range (n):
        freq[size[i]].append(i)
    # print(freq)
    """1 1 1 1 1
    p= 1 2 3 4 5
    p'= 5 1 2 3 4"""

    answer = [0] * n
    
    flag = True
    for size in freq:
        indices = freq[size]
        k = len(indices)
        if k == 1:
            flag = False
            break


        for i in range(k):
            answer[indices[i]] = indices[(i - 1) % k ] + 1

    if flag:
        print(*answer)
    else:
        print(-1)

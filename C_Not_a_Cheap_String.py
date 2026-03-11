t = int(input())

for _ in range(t):
    w = list(input())
    p = int(input())

    d = {i: v for i, v in enumerate(w)}
    w.sort()

    ps = [(ord(x)-ord('a') + 1) for x in w]
    # print(ps)

    for i in range(1,len(ps)):
        ps[i] += ps[i-1]
    
    right = 0
    # print(ps)
    while (right < len(ps)):
        if ps[right] > p:
            break
        right += 1

    freq = {}
    for ch in w[:right]:
        freq[ch] = freq.get(ch, 0) + 1

    res = []
    for key in d.keys():
        if freq.get(d[key], 0) > 0:
            res.append(d[key])
            freq[d[key]] -= 1

    print("".join(res))
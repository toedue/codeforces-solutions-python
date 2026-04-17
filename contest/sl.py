def solve():
    n = int(input())
    s = list(intput())


    t = []
    m = []
    for i,e in enumerate(s):
        if e == "T":
            t.append(i)
        else:
            m.append(i)
    
    for i in s:
        for 
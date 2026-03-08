t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    binary = [int(c) for c in s]
    
    index = [i for i in range(n) if binary[i] == 1]
    
    if not index:
        min_ones = 0
        max_ones = 0
    else:
        components = []
        current = [index[0]]

        for i in range(1, len(index)):
            if index[i] - index[i-1] <= 2:
                current.append(index[i])
            else:
                components.append(current)
                current = [index[i]]
        components.append(current)
        
        min_ones = 0
        max_ones = 0
        for comp in components:
            idx1 = comp[0]
            idxk = comp[-1]
            L = idxk - idx1 + 1
            min_ones += (L + 2) // 2
            max_ones += L
    
    print(f"{min_ones} {max_ones}")
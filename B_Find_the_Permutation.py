import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())
    deg_vertex = []

    for i in range(n):
        row = input()
        deg = row.count("1")
        deg_vertex.append((deg, i+1))
    
    # print(deg_vertex)
    deg_vertex.sort()
    # print(deg_vertex)

    result = [v for d, v in deg_vertex]

    print(*result)




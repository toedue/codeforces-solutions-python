import math

n, m, a = map(int, input().split())

w = math.ceil(n/a)
l = math.ceil(m/a)

print(w*l)
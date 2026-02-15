k, r = map(int, input().split())

i = 1

while (k * i) % 10 != r and (k *i) %10 != 0:
    i += 1

print(i)
name = input()

step = 0
current = 97

for chr in name:
    ascii = ord(chr)
    step += min(abs(ascii - current), 26 - abs(current - ascii))
    current = ascii

print(step)

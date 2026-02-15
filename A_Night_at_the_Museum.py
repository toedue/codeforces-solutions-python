name = input()

step = 0
current = 97

for chr in name:
    ascii = ord(chr)

    if abs(current - ascii) >= 13 and current < ascii:
        step += abs((current + 26) - ascii)
        current = ascii

    elif abs(current - ascii) >= 13 and current > ascii:
        step += abs(current  - (ascii + 26))
        current = ascii
    else:
        step += abs(ascii - current)
        current = ascii

print(step)

    
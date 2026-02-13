word = input()

upper_case = 0
lower_case = 0

for char in word:
    if ord(char) >= 97 and ord(char) <= 122:
        lower_case += 1
    else:
        upper_case += 1
if upper_case > lower_case:
    print(word.upper())

else:
    print(word.lower())
test_case = int(input())
for _ in range(test_case):
    word = input()
    n = len(word)

    if n <= 10:
        print(word)
    else:
        print(word[0] + str(n-2) + word[-1])

test_case = int(input())
for i in range(test_case):
    size = int(input())
    arr = list(map(str, input().split()))

    s = ""

    for word in arr:
        if s == "":
            s += word
        else:
            s1 = s + word
            s2 = word + s
            if s1 < s2:
                s = s1
            else:
                s = s2

    print(s)
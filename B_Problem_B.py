
t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))

    pointer1 = 0
    pointer2 = n -1

    arr2 = []

    while pointer1 <= pointer2:
        if pointer1 != pointer2:
            arr2.append(arr1[pointer1])
            arr2.append(arr1[pointer2])
        else:  # pointer1 = pointer2:
            arr2.append(arr1[pointer1])
        pointer1 +=1
        pointer2 -=1
    print(" ".join(map(str, arr2)))




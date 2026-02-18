test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        x = list(map(int, input().strip()))
        matrix.append(x)

    layers = min(n,m)//2
    pattern = [1, 5 ,4, 3]
    counter = 0

    for k in range(1, layers + 1):
        arr = []

        #top row
        i = k-1
        for j in range(k-1, m-k + 1):
            arr.append(matrix[i][j])

        # right column
        j = m-k
        for i in range(k, n-k + 1):
            arr.append(matrix[i][j])

        #bottom row 
        i = n-k
        for j in range(m-k-1,k-2, -1):
            arr.append(matrix[i][j])

        #left column
        j = k-1
        for i in range(n-k-1, k-1, -1):
            arr.append(matrix[i][j])

        new_arr = arr + arr

        for i in range(len(arr)):
            if new_arr[i:i + len(pattern)] == pattern:
                counter += 1

    print(counter)
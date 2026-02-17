taste_case = int(input())

for _ in range(taste_case):
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input()))
        matrix.append(row)

    answer = 0
    

    for i in range(n):
        for j in range(n):

            ones = matrix[i][j]
            ones += matrix[j][n-1-i]
            ones += matrix[n-1-i][n-1-j]
            ones += matrix[n-1-j][i]

            zeros = 4 - ones

            answer += min(ones, zeros)


    print(answer//4)





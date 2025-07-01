n = int(input())
matrix = []

for i in range (n):
    row = list(map(int,input().split()))
    matrix.append(row)

sum = 0
mid = n//2

for i in range(n):
    sum += matrix[i][i]
    matrix[i][i] =0

for i in range(n):
    sum += matrix [i][n-1-i]
    matrix [i][n-1-i] =0

for i in range(n):
    sum += matrix [mid][i]
    matrix [mid][i] =0

for i in range(n):
    sum += matrix [i][mid]
    matrix [i][mid] =0

print(sum)



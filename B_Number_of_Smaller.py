n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ptr1 = 0
ptr2 = 0
count = 0
result = []


while ptr1 < n and ptr2 < m:
        if arr1[ptr1] < arr2[ptr2]:
            count += 1
            ptr1 += 1
        else:
            result.append(count)
            ptr2 += 1

for i in range(ptr2, m):
    result.append(count)

print(*result)


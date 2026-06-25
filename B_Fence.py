n, k = map(int, input().split())

planks = list(map(int, input().split()))


current_sum = sum(planks[:k])
min_sum = current_sum
index = 0

for i in range(1,len(planks)-k+1):
    current_sum = current_sum - planks[i-1] + planks[i+k-1]
    if current_sum < min_sum:
        min_sum = current_sum
        index = i

print(index + 1)
n,h = map(int, input().split())
friends = map(int, input().split())

sum =0
for height in friends:
    if height > h:
        sum += 2
    else:
        sum += 1
        
print(sum)
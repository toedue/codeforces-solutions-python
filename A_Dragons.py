kiritos_strength, n = map(int, input().split())
dragons = []
canFight = True
for i in range (n):
    x, y = map(int, input().split())
    dragons.append((x,y))


# print(f"initial kiritos_strength is {kiritos_strength}")  
# print(dragons)


sortedDragons = sorted(dragons, key=lambda x: x[0])

# print(sortedDragons)

for dragon in sortedDragons:
    if kiritos_strength > dragon[0]:
        kiritos_strength += dragon[1]
    else:
        canFight = False
        break

if canFight:
    print("YES")
else:
    print("NO")
    
limak, bob = map(int, input().split())

counter = 0
while (limak <= bob):
    limak = 3*limak
    bob = 2*bob
    counter +=1

print(counter)
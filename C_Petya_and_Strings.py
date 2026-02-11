first_string = input() 
second_string = input()

lowercase1 = first_string.lower()
lowercase2 = second_string.lower()

# print(lowercase1)
# print(lowercase2)

if lowercase1 < lowercase2:
    print(-1)
elif lowercase2 < lowercase1:
    print (1)
else:
    print(0)
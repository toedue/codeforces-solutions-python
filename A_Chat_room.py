str1 = input()
str2 = "hello"
j = 0
for i in range(len(str1)):
    if str1[i] == str2[j]:
        j +=1
    if j == 5:
        break
if j == 5:
    print("YES")
else:
    print("NO")

        
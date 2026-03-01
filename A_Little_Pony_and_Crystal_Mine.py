n = int(input())

# for i in range(n):
#     diamonds = n - abs(n//2 -i)*2
#     stars = (n-diamonds) // 2
#     print ("*"* stars + "D"*diamonds + "*"*stars)
center = n // 2

for i in range(n):
    distance = abs(center - i)
    diamond = n - 2 * distance
    stars = distance
    print("*"*stars+ "D"*diamond + "*"*stars)
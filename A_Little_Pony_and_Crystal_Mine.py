n = int(input())

for i in range(n):
    diamonds = n - abs(n//2 -i)*2
    stars = (n-diamonds) // 2
    print ("*"* stars + "D"*diamonds + "*"*stars)
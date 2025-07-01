t = int(input())
for i in range(t):
    x,y = input().split()

    if x==y:
        print("=")
    elif x[-1] == 'L' and  y[-1]== 'M':
        print(">")
    elif x[-1] =='L' and  y[-1]== 'S':
        print(">")
    elif  x[-1] =='L' and  y[-1]== 'L':
        if len(x) > len(y):
            print(">")
        else:
            print("<")
    elif x[-1] =='M' and  y[-1]== 'L':
        print("<")
    elif x[-1] =='M' and  y[-1]== 'S':
        print(">")
    elif x[-1] =='M' and  y[-1]== 'M':
        if len(x) > len(y):
            print(">")
        else:
            print("<")
    elif x[-1] =='S' and  y[-1]== 'L':
        print("<")
    elif x[-1] =='S' and  y[-1]== 'M':
        print("<")
    elif x[-1] =='S' and  y[-1]== 'S':
        if len(x) > len(y):
            print("<")
        else:
            print(">")



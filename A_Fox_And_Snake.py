n, m = map(int, input().split())


def draw (row, n, m , right):
    if row > n:
        return
    
    if row % 2 == 1:
        print('#'* m)

    else:
        if right:
            print('.'* (m-1) + '#')
        else:
            print('#' + '.'*(m-1))
        right = not right

    draw(row + 1, n, m , right)

draw (1, n , m , True)
    



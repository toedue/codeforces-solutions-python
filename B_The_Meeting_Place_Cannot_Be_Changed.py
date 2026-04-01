n = int(input())

coordinates = list(map(int, input().split()))
speeds = list(map(int, input().split()))
coordinaresSpeed = list(zip(coordinates, speeds))
coordinaresSpeed.sort()

# print(coordinaresSpeed)

ans = -1
low = 0
high = 1e9

def check(time):
    first_coordinate = coordinaresSpeed[0][0]
    first_speed = coordinaresSpeed[0][1]
    range_ = [first_coordinate- first_speed * time, first_coordinate + first_speed * time]

    for i in range(1, n):
        i_coordinate = coordinaresSpeed[i][0]
        i_speed = coordinaresSpeed[i][1]
        irange = [i_coordinate- i_speed * time, i_coordinate + i_speed * time]

        if irange[0] > range_[1]:
            return False
        
        # update the range 
        range_ = [max(irange[0],range_[0]), min(irange[1], range_[1])]

    return True




while high - low > 1e-7: # 10** -6
    mid = (high + low) / 2
    if check(mid):
        ans = mid 
        high = mid
    else:
        low = mid

print(ans)
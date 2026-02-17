t = int(input())

for _ in range(t):
    n = int(input())

    alice = 1
    bob = 0

    remaining = n- 1
    
    """pattern: 5, 9, 13, 17, 21, ...  """  
    take = 5

    bobs_turn = True
    
    while (remaining > 0):

        current = min(remaining, take)

        if bobs_turn:
            bob += current

        else:
            alice += current

        remaining -= current
        take += 4
        bobs_turn = not bobs_turn

    print(alice , bob)



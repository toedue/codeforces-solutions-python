t = int(input())

for _ in range(t):
    n = int(input())
    
    white_alice = 0
    black_alice = 0
    white_bob = 0
    black_bob = 0
    
    cards_to_give= 1
    cards_counted = 0
    turn = 0       # 0 = Alice, 1 = Bob
    
    for pos in range(1, n + 1):
        if turn == 0:
            if pos % 2 == 1:
                white_alice += 1
            else:
                black_alice += 1
        else:
            if pos % 2 == 1:
                white_bob += 1
            else:
                black_bob += 1
        
        cards_counted += 1
        
        if cards_counted == cards_to_give:
            cards_to_give += 1
            cards_counted = 0
            if cards_to_give % 2 == 0:
                turn = 1 - turn
    
    print(white_alice, black_alice, white_bob, black_bob)
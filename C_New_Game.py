from collections import Counter

t = int(input())

for _ in range (t):
    n , k = map(int , input().split())

    decks = list(map(int, input().split()))

    frq = Counter(decks)

    #get unique values and sort them
    unique = sorted(frq.keys())

    max_cards = 0
    current = 0
    left = 0









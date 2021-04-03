import random, itertools

cards = list(itertools.product(range(1, 14), ["spades", "diamonds", "clubs", "hearts"]))
random.shuffle(cards)
for n in range(52):
    print(f"{cards[n][0]} of {cards[n][1]}")
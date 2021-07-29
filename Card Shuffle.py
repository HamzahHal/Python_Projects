import random
import itertools

deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# randomise and shuffle the deck variable between the range of 1-14 and between card types
random.shuffle(deck)

# print the shuffled cards
print('you got')
for i in range(5):
    print(deck[i][0], 'of', deck[i][1])

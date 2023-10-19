cards_deck = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_index = int(len(cards_deck) // 2)
    first_half = cards_deck[:middle_index]
    second_half = cards_deck[middle_index:]
    new_cards_deck = []
    if len(cards_deck) % 2 == 0:
        for card in range(len(first_half)):
            new_cards_deck.append(first_half[card])
            new_cards_deck.append(second_half[card])
            cards_deck = new_cards_deck

print(cards_deck)



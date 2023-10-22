def deck_of_cards(cards, num_of_commands):
    for i in range(num_of_commands):
        command = input().split(', ')
        if command[0] == 'Add':
            card_name = command[1]
            if card_name not in cards:
                cards.append(card_name)
                print('Card successfully added')
            else:
                print('Card is already in the deck')

        elif command[0] == 'Remove':
            card_name = command[1]
            if card_name in cards:
                cards.remove(card_name)
                print('Card successfully removed')
            else:
                print('Card not found')

        elif command[0] == 'Remove At':
            idx = int(command[1])
            if 0 <= idx < len(cards):
                removed_card = cards.pop(idx)
                print('Card successfully removed')
            else:
                print('Index out of range')

        elif command[0] == 'Insert':
            idx = int(command[1])
            card_name = command[2]
            if 0 <= idx < len(cards):
                if card_name in cards:
                    print('Card is already added')
                else:
                    cards.insert(idx, card_name)
                    print('Card successfully added')
            else:
                print('Index out of range')

    return ', '.join(cards)


list_of_cards = input().split(', ')
number_of_commands = int(input())

print(deck_of_cards(list_of_cards, number_of_commands))
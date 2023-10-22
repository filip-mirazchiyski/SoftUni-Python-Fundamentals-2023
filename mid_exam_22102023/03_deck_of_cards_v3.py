def add_func(card):
    if current_command[1] not in list_of_cards:
        list_of_cards.append(current_command[1])
        print("Card successfully added")
    else:
        print("Card is already in the deck")


def remove_func(card):
    if current_command[1] in list_of_cards:
        list_of_cards.remove(current_command[1])
        print("Card successfully removed")
    else:
        print("Card not found")


def remove_at_func(index, card):
    if int(current_command[1]) <= len(list_of_cards) - 1:
        list_of_cards.remove(list_of_cards[int(current_command[1])])
        print("Card successfully removed")
    else:
        print("Index out of range")


def insert_func(index, card):
    if int(current_command[1]) <= len(list_of_cards) - 1 and current_command[2] in list_of_cards:
        print("Card is already added")
    elif int(current_command[1]) <= len(list_of_cards) - 1 and current_command[2] not in list_of_cards:
        list_of_cards.insert(int(current_command[1]), current_command[2])
        print("Card successfully added")
    else:
        print("Index out of range")


list_of_cards = input().split(', ')
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split(", ")
    if current_command[0] == "Add":
        card = current_command[1]
        add_func(card)
    elif current_command[0] == "Remove":
        card = current_command[1]
        remove_func(card)
    elif current_command[0] == "Remove At":
        index, card = current_command[0], current_command[1]
        remove_at_func(index, card)
    elif current_command[0] == "Insert":
        index, card = current_command[1], current_command[2]
        insert_func(index, card)

print(", ".join(list_of_cards))

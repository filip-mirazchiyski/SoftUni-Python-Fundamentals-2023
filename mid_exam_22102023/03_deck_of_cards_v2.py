list_of_cards = input().split(', ')
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split(", ")
    if current_command[0] == "Add":
        if current_command[1] not in list_of_cards:
            list_of_cards.append(current_command[1])
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif current_command[0] == "Remove":
        if current_command[1] in list_of_cards:
            list_of_cards.remove(current_command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    elif current_command[0] == "Remove At":
        if int(current_command[1]) <= len(list_of_cards) - 1:
            list_of_cards.remove(list_of_cards[int(current_command[1])])
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif current_command[0] == "Insert":
        if int(current_command[1]) <= len(list_of_cards) - 1 and current_command[2] in list_of_cards:
            print("Card is already added")
        elif int(current_command[1]) <= len(list_of_cards) - 1 and current_command[2] not in list_of_cards:
            list_of_cards.insert(int(current_command[1]), current_command[2])
            print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))

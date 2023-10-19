team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

cards = input()
cards_list = (list(cards.split(" "))) # We split the integer and add in a list

# Using remove() method to remove common elements
for i in cards_list[:]:
    if (i in team_A):
        team_A.remove(i)
    elif i in cards_list[:]:
        if (i in team_B):
            team_B.remove(i)

A_players_left = len(team_A)
B_players_left = len(team_B)

print(f"Team A - {A_players_left}; Team B - {B_players_left}")

    if A_players_left < 7 or B_players_left < 7:
        print("Game was terminated")
        break

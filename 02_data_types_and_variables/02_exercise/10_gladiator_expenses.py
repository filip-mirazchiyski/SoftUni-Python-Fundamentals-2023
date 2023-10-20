lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repair = 0
sword_repair = 0
shield_repair = 0
armor_repair = 0

shield_break_counter = 0

for lost_fight in range (1, lost_fights + 1):
    if lost_fight % 2 == 0:
        helmet_repair += helmet_price
    if lost_fight % 3 == 0:
        sword_repair += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        shield_repair += shield_price
        shield_break_counter += 1
    if shield_break_counter > 0 and shield_break_counter % 2 == 0:
        armor_repair += armor_price
        shield_break_counter = 0

total_repair = helmet_repair + sword_repair + shield_repair + armor_repair
print(f"Gladiator expenses: {total_repair:.2f} aureus")

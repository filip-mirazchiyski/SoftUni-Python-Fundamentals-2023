recruited_heroes = {}

command = input().split()

while command[0] != "End":

    if command[0] == "Enroll":
        hero_name = command[1]
        if hero_name in recruited_heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            recruited_heroes[hero_name] = list()

    elif command[0] == "Learn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in recruited_heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in recruited_heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            recruited_heroes[hero_name].append(spell_name)

    elif command[0] == "Unlearn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in recruited_heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in recruited_heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            recruited_heroes[hero_name].remove(spell_name)

    command = input().split()

if recruited_heroes:
    print("Heroes:")
    for hero, spells in recruited_heroes.items():
        print(f"== {hero}: {', '.join([spell for spell in spells])}")

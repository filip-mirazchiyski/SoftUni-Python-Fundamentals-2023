import re

information = input()
pattern = r"([#|@]+)([a-z]{3,})([#|@]+)([\D\W]+)\/+(\d+)\/+"
matches = re.findall(pattern, information)

for element in matches:
    egg_color = element[1]
    egg_count = element[4]
    print(f"You found {egg_count} {egg_color} eggs!")
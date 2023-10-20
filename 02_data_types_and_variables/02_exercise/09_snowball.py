count_of_snowballs = int(input())
snowball_value = 0
max_snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for i in range (1, count_of_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = (weight / time) ** quality
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_snowball_value:.0f} ({max_quality})")


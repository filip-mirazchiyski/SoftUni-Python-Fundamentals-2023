budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
loaf_price = eggs_price + flour_price + milk_price / 4
bread_counter = 0
colored_eggs_counter = 0
remaining_budget = budget


while remaining_budget > loaf_price:
    bread_counter += 1
    colored_eggs_counter += 3
    remaining_budget -= loaf_price
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {remaining_budget:.2f}BGN left.")
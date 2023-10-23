cities = int(input())
total_money = 0
current_money = 0

for city in range(1, cities + 1):
    city_name = input()
    money_earned = float(input())
    money_spent = float(input())
    if city % 3 == 0:
        if city % 5 != 0:
            money_spent *= 1.5
        else:
            money_spent = money_spent
            money_earned *= 0.9
    if city % 5 == 0:
        money_earned *= 0.9
    current_money += round(money_earned, 2)
    current_money -= round(money_spent, 2)
    total_money += round(money_earned, 2)
    total_money -= round(money_spent, 2)
    print(f"In {city_name} Burger Bus earned {current_money:.2f} leva.")
    current_money = 0
print(f"Burger Bus total profit: {total_money:.2f} leva.")


coffee_price = 1.5
water_price = 1.0
coke_price = 1.4
snacks_price = 2.0
total_price = 0

def calculate_total_price(product, quantity):
    if product == "coffee":
        return f"{coffee_price * quantity:.2f}"
    elif product == "water":
        return f"{water_price * quantity:.2f}"
    elif product == "coke":
        return f"{coke_price * quantity:.2f}"
    elif product == "snacks":
        return f"{snacks_price * quantity:.2f}"

product = input()
quantity = int(input())
result = calculate_total_price(product, quantity)
print(result)
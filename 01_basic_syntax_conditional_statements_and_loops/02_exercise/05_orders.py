orders_count = int(input())
total = 0

for i in range(1, orders_count + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsues_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.0 or days < 1 or days > 31 or capsues_needed_per_day < 1 or capsues_needed_per_day > 2000:
        continue
    price = price_per_capsule * days * capsues_needed_per_day
    total += price
    print(f"The price for the coffee is: ${price:.2f}")
print("Total: $%.2f" % total)

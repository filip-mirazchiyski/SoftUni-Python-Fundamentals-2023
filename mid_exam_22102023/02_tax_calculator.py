vehicles_as_string = input().split('>>')
initial_tax = 0
current_vehicle_collected_tax = 0
total_collected_tax = 0

for vehicle in vehicles_as_string:
    vehicle_data = vehicle.split()
    vehicle_type = vehicle_data[0]
    years_to_pay_tax = int(vehicle_data[1])
    km_travelled = int(vehicle_data[2])

    if vehicle_type == 'family':
        initial_tax = 50
        tax_increase_count = km_travelled // 3000
        current_vehicle_collected_tax = initial_tax + (tax_increase_count * 12) - (years_to_pay_tax * 5)

    elif vehicle_type == 'heavyDuty':
        initial_tax = 80
        tax_increase_count = km_travelled // 9000
        current_vehicle_collected_tax = initial_tax + (tax_increase_count * 14) - (years_to_pay_tax * 8)

    elif vehicle_type == 'sports':
        initial_tax = 100
        tax_increase_count = km_travelled // 2000
        current_vehicle_collected_tax = initial_tax + (tax_increase_count * 18) - (years_to_pay_tax * 9)

    else:
        print("Invalid car type.")
        continue

    total_collected_tax += current_vehicle_collected_tax

    print(f"A {vehicle_type} car will pay {current_vehicle_collected_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_collected_tax:.2f} euros in taxes.")
max_capacity = 255
actual_capacity = 0
n = int(input())
for i in range(n):
    litres_added = int(input())
    if litres_added < max_capacity and actual_capacity <= max_capacity:
        actual_capacity += litres_added
        if actual_capacity <= 255:
            continue
        else:
            actual_capacity -= litres_added
            print("Insufficient capacity!")
    else:
        print("Insufficient capacity!")
print(actual_capacity)
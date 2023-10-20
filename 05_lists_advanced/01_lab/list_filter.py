numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter(lambda number: number % 2 != 0, numbers)

print(list(odd_numbers))

###

names = ["Asen", "Ivan", "Angel", "Plamen", "Ani"]

filtered_names = list(filter(lambda name: name.startswith("A"), names))

print(filtered_names)
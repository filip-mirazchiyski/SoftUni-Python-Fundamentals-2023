numbers = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3

numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

print(numbers)
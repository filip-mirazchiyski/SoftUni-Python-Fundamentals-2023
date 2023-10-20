nums = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in nums]
squares_even = [num ** 2 for num in nums if num % 2 == 0]
squares_odd = [num ** 2 for num in nums if num % 2 != 0]
print(squares)
print(squares_even)
print(squares_odd)

#######################################

letters = ["a", "b", "c", "d"]
uppercase = [letter.upper() for letter in letters]
print(uppercase)

#######################################

even_nums = [num for num in list(map(int, input().split(", "))) if num % 2 == 0]
print(even_nums)

#######################################

nums = [1, 2, 3, 4]
result = [num ** 2 if num % 2 == 0 else num ** 3 for num in nums]
print(result)

#######################################

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print([num for num in b])
print([num for num in b if num % 2 == 0])
print([num if num % 2 == 0 else num ** 2 for num in b]) # if we have if-else, the order is different
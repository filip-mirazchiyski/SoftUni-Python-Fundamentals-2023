numbers_as_string = input().split()
nums_to_remove = int(input())
numbers_as_integers = []
smallest_int = 0
final_result = []

# Turning the String List to an Integer List
for current_number in numbers_as_string:
    numbers_as_integers.append(int(current_number))

for nums in range(nums_to_remove):
    numbers_as_integers.remove(min(numbers_as_integers))

for current_number in numbers_as_integers:
    final_result.append(str(current_number))

result = str(', '.join(final_result))
print(result)
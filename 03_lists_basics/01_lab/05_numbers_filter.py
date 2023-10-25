count_of_nums = int(input())
list_of_nums = []

for num in range(count_of_nums):
    current_num = int(input())
    list_of_nums.append(current_num)

command = input()

if command == "even":
    for i in range(len(list_of_nums) - 1, -1, -1):
        element = list_of_nums[i]
        if element % 2 != 0:
            list_of_nums.remove(element)
    print(list_of_nums)
elif command == "odd":
    for i in range(len(list_of_nums) - 1, -1, -1):
        element = list_of_nums[i]
        if element % 2 == 0:
            list_of_nums.remove(element)
    print(list_of_nums)
elif command == "positive":
    for i in range(len(list_of_nums) - 1, -1, -1):
        element = list_of_nums[i]
        if element < 0:
            list_of_nums.remove(element)
    print(list_of_nums)
elif command == "negative":
    for i in range(len(list_of_nums) - 1, -1, -1):
        element = list_of_nums[i]
        if element >= 0:
            list_of_nums.remove(element)
    print(list_of_nums)

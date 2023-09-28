first_num = int(input())
second_num = int(input())
third_num = int(input())
largest_num = 0
if first_num > second_num and first_num > third_num:
    largest_num = first_num
    print(largest_num)
elif second_num > first_num and second_num > third_num:
    largest_num = second_num
    print(largest_num)
elif third_num > first_num and third_num > second_num:
    largest_num = third_num
    print(largest_num)

#num1, num2, num3 = int(input()), int(input()), int(input())
#largest = max(num1, num2, num3)
#print(largest)
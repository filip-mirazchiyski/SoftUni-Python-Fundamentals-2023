number_of_lines = int(input())
sum_of_ascii = 0
for i in range(number_of_lines):
     char = input()
     sum_of_ascii += ord(char)
print(f"The sum equals: {sum_of_ascii}")
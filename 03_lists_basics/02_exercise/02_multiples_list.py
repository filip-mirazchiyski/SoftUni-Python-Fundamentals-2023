factor = int(input())
count = int(input())
my_list = []
new_num = 0

for i in range (count):
    new_num = new_num + factor
    my_list.append(new_num)

print(my_list)
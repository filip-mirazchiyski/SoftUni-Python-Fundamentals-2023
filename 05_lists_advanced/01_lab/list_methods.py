my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list = [1, 2, 3]
my_list.insert(0, 22) #index, value
print(my_list)

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

my_list = [1, 2, 3]
my_list.pop()
print(my_list)

my_list = [1, 2, 3]
my_list.extend([4])
print(my_list)

fruits = ["apple", "banana", "orange", "banana", "banana"]
number_of_bananas = fruits.count("banana")
element_index = fruits.index("orange") # always returns the first index it finds it at
element_index = fruits.index("orange", 1) # specifying an index to start the search from
print(number_of_bananas)
print(element_index)

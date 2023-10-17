def rounding_numbers():
    string = input()
    my_list = (list(string.split(" ")))  # We split the integer and add in a list
    int_list = [float(i) for i in my_list]  # We turn the list values from Strings to Integers using List comprehension
    new_list = []  # We create a new empty list

    for number in int_list:  # We iterate through the int_list and check each number if it is + or -
        new_list.append(round(number))  # If number is positive, reverse its value and add to new list
    print(new_list)

rounding_numbers()

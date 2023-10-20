number_of_letters = int(input())

for letter1 in range (0, number_of_letters):
    for letter2 in range (0, number_of_letters):
        for letter3 in range (0, number_of_letters):
            print(f"{chr(97+letter1)}{chr(97+letter2)}{chr(97+letter3)}")
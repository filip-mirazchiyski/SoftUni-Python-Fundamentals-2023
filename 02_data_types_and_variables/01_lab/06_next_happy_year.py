year = int(input())
year_is_special = False

while year_is_special == False:
    year += 1
    year_as_string = str(year)
    for digit in year_as_string:
        if year_as_string.count(digit) != 1:
            break
    else: year_is_special = True
print(year)

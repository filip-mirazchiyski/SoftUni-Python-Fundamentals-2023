n = int(input())

for i in range(1, n + 1):
    string = input()
    count_1 = string.count(",")
    count_2 = string.count(".")
    count_3 = string.count("_")
    if count_1 == 0 and count_2 == 0 and count_3 == 0:
        print(string + " is pure.")
    else:
        print(string + " is not pure!")


n = int(input())

for i in range(1, n + 1):
    string = input()

    if "," in string or "." in string or "_" in string:
        print(string + " is not pure!.")
    else:
        print(string + " is pure.")
print("1. Draw a Triangle\n2. Draw a Rectangle\n3. Draw a Pyramid\n4. Quit")
choice = int(input("\nEnter your choice (1/2/3/4): "))
if choice == 1:
    print("You've selected triangle")
    rows = int(input("Enter the number of rows for the triangle: "))
    rotation = input("Enter 'u' for upward or 'd' for downward: ")
    if rotation == "u":
        for i in range(1, rows + 1):
            for j in range(0, i):
                print("*", end="")
            print()
    elif rotation == "d":
        for i in range(rows - 1, 0, -1):
            for j in range(0, i):
                print("*", end="")
            print()

choice = int(input("Enter your choice (1/2/3/4): "))
if choice == 2:
    print("You've selected rectangle")
    rows = int(input("Enter the number of rows for the rectangle: "))
    columns = int(input("Enter the number of columns for the rectangle: "))
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print()

choice = int(input("Enter your choice (1/2/3/4): "))
if choice == 3:
    print("You've selected pyramid")
    rows = int(input("Enter the number of rows for the pyramid: "))
    k = 0
    for i in range(1, rows + 1):
        for space in range(1, (rows - i) + 1):
            print(end="  ")
        while k != (2 * i - 1):
            print("* ", end="")
            k += 1
        k = 0
        print()

choice = int(input("Enter your choice (1/2/3/4): "))
if choice == 4:
    print("Goodbye!")
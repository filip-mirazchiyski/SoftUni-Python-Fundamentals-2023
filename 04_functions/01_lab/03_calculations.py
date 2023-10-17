def calculations():
    operator = input()
    num1 = float(input())
    num2 = float(input())
    result = 0

    if operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    elif operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 / num2

    print(int(result))

calculations()
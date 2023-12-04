def decode_message(message, commands):

    for command in commands:
        tokens = command.split()
        instruction = tokens[0]

        if instruction == "Change":
            char = tokens[1]
            replacement = tokens[2]
            message = message.replace(char, replacement)
            print(message)


        elif instruction == "Includes":
            substring = tokens[1]
            if substring in message:
                print(True)
            else:
                print(False)

        elif instruction == "End":
            substring = tokens[1]
            print(message.endswith(substring))


        elif instruction == "Uppercase":
            new_message = message.upper()
            print(new_message)
            message = new_message

        elif instruction == "FindIndex":
            char = tokens[1]
            if char in message:
                print(message.index(char))

        elif instruction == "Cut":
            startIndex = tokens[1]
            count = tokens[2]
            endIndex = int(startIndex) + int(count)
            print(message[int(startIndex):endIndex])


string = input()
commands_list = []

while True:
    command = input()
    commands_list.append(command)

    if command == "Done":
        break

decode_message(string, commands_list)
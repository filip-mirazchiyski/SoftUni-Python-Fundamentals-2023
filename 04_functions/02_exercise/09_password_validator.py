def password_validator(some_password: str) -> str:
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum(): # built in function to check if something has only letters and nums
        list_of_errors.append("Password must consist only of letters and digits")
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter += 1

    if digits_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
validatated_password = password_validator(password)

if len(validatated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validatated_password))
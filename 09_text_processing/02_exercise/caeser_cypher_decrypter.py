message = input()

encrypted_message = ""
decrypted_message = ""

for character in message:
    encrypted_character = chr(ord(character) + 3)
    encrypted_message += encrypted_character

print(encrypted_message)

for character in encrypted_message:
    decrypted_character = chr(ord(character) - 3)
    decrypted_message += decrypted_character

print(decrypted_message)


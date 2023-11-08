sequence = input().split()

new_sequence = [txt *(len(txt)) for txt in sequence]
print("".join(new_sequence))
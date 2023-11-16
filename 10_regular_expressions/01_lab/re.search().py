import re

string = "The quick brown fox jumps over the lazy dog. Python is fun. Programming."

match = re.search(r'\\bp\\w*', string, re.IGNORECASE)

if match:
    print(f'The first word that starts with "p" is: {match.groups()}')
else:
    print('No words starting with "p".')
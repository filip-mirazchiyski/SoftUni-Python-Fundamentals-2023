import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?((?=\s)|$)"
string = input()
matches = re.finditer(pattern, string)
for match in matches:
    print(match.group(), end= " ")
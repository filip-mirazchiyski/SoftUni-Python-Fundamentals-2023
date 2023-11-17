import re

some_string = "somesite"
result = re.search(r"some(?=[a-z]+)", some_string)

print(result.group())
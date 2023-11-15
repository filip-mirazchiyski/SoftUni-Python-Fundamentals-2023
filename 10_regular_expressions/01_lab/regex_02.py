import re

text = "Python is an interpreted language."
pattern = "[arn]"
result = re.findall(pattern, text)
print(result)

text = "Python is an interpreted language."
pattern = "[^arn]"
result = re.findall(pattern, text)
print(result)

text = "Python is an interpreted language. 22"
pattern = "[0123]"
result = re.findall(pattern, text)
print(result)

text = "19:47"
pattern = "[0-5][0-9]"
result = re.findall(pattern, text)
print(result)
import re

text = "abc def"
pattern = "ab"
result = re.findall(pattern, text)
print(result)

text = "dog, cat, bird, snake"
pattern = "dog|cat"
result = re.findall(pattern, text)
print(result)

text = "The ball is red and big, end of text"
pattern = "(red|blue) and (big|small)"
result = re.findall(pattern, text)
print(result)

text = "Python is fun."
pattern = "fun\.$"
result = re.findall(pattern, text)
print(result)

text = "Python is fun."
pattern = "^Python"
result = re.findall(pattern, text)
print(result)
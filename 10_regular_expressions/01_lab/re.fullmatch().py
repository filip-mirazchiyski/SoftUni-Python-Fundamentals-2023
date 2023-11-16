import re
string = """
^               # start of string
(20|30)\d\d     # year
-               # separator
(0[1-9]|1[012])
-
(0[1-9]|[12][0-9]|3[01])
$
"""

text = "2022-7-12"

print(re.fullmatch(string, text, re.X))
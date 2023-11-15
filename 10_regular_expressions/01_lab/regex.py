import re
def regex_func(regex, string):
    match = re.search(regex, string)

    if match:
        print("Match found:", match.group())
    else:
        print("No match found!")

regex_func("\d", "Ivan88")
regex_func("\d+", "Ivan88")
regex_func("\D", "Ivan88")
regex_func("\D+", "Ivan88")
regex_func("\\world\\b", "hello world dasdas")
regex_func("\s", "hello world dasdas")
regex_func("\S", "hello world dasdas")
regex_func("\S+", "hello world dasdas")
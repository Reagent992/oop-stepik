import re


string = "абв123дежз"
pattern = r"[а-я]+(\d+)[а-я]+"
m = re.search(pattern, string)
if m:
    print(m.group(0))
    print(m.group(1))

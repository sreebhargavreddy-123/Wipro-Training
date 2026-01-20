import re

text = "Python is fun"
result = re.match("Python", text)
if result:
    print("match found")
else:
    print("no match found")

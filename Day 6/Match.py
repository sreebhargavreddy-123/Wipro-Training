import re

text = "Python is fun"
result = re.match("Java", text)
if result:
    print("match found")
else:
    print("match not found")

searchresult = re.search("Python", text)
print(searchresult.group())
import json

data = {
    "name": "Bhargav",
    "Age" : 24,
    "Skills" : ["Python","Java"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
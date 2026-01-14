import csv
with open ("students.csv", "w",newline="") as file:
   writer = csv.writer(file)
   writer.writerow(["Name", "ID", "Age"])
   writer.writerow(["Bhargav", "1", "19"])
   writer.writerow(["Ravi", "2", "19"])
   writer.writerow(["Ram", "3", "19"])
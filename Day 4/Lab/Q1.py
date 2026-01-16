# Define the Student class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("-" * 20)


# Create objects of the Student class
student1 = Student("Bhargav", 101)
student2 = Student("Ram", 102)

# Display student details
student1.display_details()
student2.display_details()
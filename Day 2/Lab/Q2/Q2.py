class PositiveSalary:
    def __get__(self, instance, owner):
        return instance.__dict__.get("_salary")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance.__dict__["_salary"] = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Demonstration
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 65000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

# This will raise ValueError
# emp3 = Employee("Charlie", -30000)

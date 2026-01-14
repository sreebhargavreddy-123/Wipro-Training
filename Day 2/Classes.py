class student:   #without Constructor
        name = "Bhargav"
        age = 24

s1 = student()
print(s1.name)
print(s1.age)


class employee:  #With Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
emp = employee("Sree",25)
print(emp.name)
print(emp.age)
print(emp.name, emp.age)
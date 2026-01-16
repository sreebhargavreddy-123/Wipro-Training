from abc import ABC, abstractmethod

class shape(ABC):
    def  display(self):
        print("display method is implemented")
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        print("area method is implemented")

r=Rectangle()
r.area()
r.display()
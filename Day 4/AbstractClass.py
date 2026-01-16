from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        print("area method is implemented")

r=Rectangle()
r.area()
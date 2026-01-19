class box:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value

b = box(40)
b1 = box(10)
print(b + b1)

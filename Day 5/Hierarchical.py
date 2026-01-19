class parent:
    def parent1(self):
        print("parent1")

class child1(parent):
    def c1(self):
        print("child1")

class child2(parent):
    def c2(self):
        print("child2")

c1 = child1()
c1.c1()
c1.parent1()

c2 = child2()
c2.c2()
c2.parent1()
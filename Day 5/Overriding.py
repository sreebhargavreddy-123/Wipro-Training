class animal:
    def sound(self):
        print("animal sound")

class dog:
    def sound(self):
        print("dog barks")
class cat:
    def sound(self):
        print("cat meow")

obj = [dog(),cat()]

for a in obj:
    a.sound()
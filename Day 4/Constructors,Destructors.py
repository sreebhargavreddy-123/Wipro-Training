class employee:
    def __init__(self,name):
        self.name = name
        print("Constructor is Called")

    def __del__(self):
        print("Destructor is Called")

e = employee("Bhargav")
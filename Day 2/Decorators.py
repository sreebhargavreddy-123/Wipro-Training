def mydecorator(func):
    def wrapper():
        print("Before calling function")
        func()
        print("After calling function")
    return wrapper

@mydecorator
def sayhello():
    print("Hello World")
sayhello()


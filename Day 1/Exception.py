try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("can't divide by zero")

try:
    x = int(input("Enter a number"))
    print(10 / x)
except ValueError:
    print("invalid entery")

except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("Excecution is successull")


class MyError(Exception):
    pass
#raise MyError("This is a user defined Exception")

class invalidage(Exception):
    pass



try:
    age=int(input("Enter your age"))
    if age<18:
        raise invalidage("Age must be 18 or above")
    else:
        print("eligible to vote")
except invalidage as e:
    print("Error:",e)
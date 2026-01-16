def add(a,b):
    print("Add :",a+b)

def sub(a,b):
    return a-b,a

add(100,500)
print("Sub :",sub(10,5))


def hello(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))

hello()
hello('Greetings')
hello('Greetings','Bhargav')


def print_params(*params):
    print(params)
print_params('Testing')
print_params(1, 2, 3,4)


def print_params_1(**params):
    print(params)
print_params_1(x=1, y=2, z=3)

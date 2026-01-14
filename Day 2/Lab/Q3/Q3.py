import time

def execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()

        print("Function Name:", func.__name__)
        print("Execution Time:", end_time - start_time, "seconds")

    return wrapper


@execution_time
def sample_function():
    for i in range(1, 1000000):
        pass


sample_function()

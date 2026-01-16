import threading
from unittest import result


def task():
    print("threading is running")
t1= threading.Thread(target=task)
# t2= threading.Thread(target=task, args=("thread2",))
t1.start()
# t2.start()
t1.join()
# t2.join()

print("Main thread is done")
import threading
from threading import *
from time import sleep

class First_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"This is 1st thread")
            sleep(2)

class Second_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"This is 2nd thread")
            sleep(2)

t1=First_thread()
t2=Second_thread()

t1.start()
print(t1.is_alive())
t2.start()
print(t2.is_alive())
t1.join()
t2.join()
print(t1.is_alive())
print(t2.is_alive())

import threading
print(threading.current_thread().getName())
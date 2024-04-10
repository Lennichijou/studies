from threading import *
import time

sem = Semaphore(4)


def show(the_name):
    sem.acquire()
    for n in range(6):
        print('Sample Text, ', end='')
        time.sleep(1)
        print(the_name)
        sem.release()


thread_1 = Thread(target=show, args=('Thread 1 ',))
thread_2 = Thread(target=show, args=('Thread 2 ',))
thread_3 = Thread(target=show, args=('Thread 3 ',))
thread_4 = Thread(target=show, args=('Thread 4 ',))
thread_5 = Thread(target=show, args=('Thread 5 ',))
thread_6 = Thread(target=show, args=('Thread 6 ',))


thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
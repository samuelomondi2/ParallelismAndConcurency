
import threading
import time

def thread_function(name):
    print(f'Thread: {name} starting')
    time.sleep(2)
    print(f'Thread: {name} finishing')

if __name__ == '__main__':
    print('Main: before creating thread')
    t = threading.Thread(target=thread_function, args=('Samuel',))
    print('Main: before running the thread')

    t.start()

    print('Main: wait for the thread to finish')
    t.join()
    print('Main: all done!')


"""
PROGRAM OUTPUT:

Main    : before creating thread
Main    : before running thread
Thread "Samuel": starting
Main    : wait for the thread to finish
Thread "Samuel": finishing
Main    : all done!

"""



# Creating multiple threads example

def multiple_thread_function(name, sleep_time):
    print(f'Thread: {name} starting')
    time.sleep(sleep_time)
    print(f'Thread: {name} finishing')

if __name__ == '__main__':
    print('Main: before creating thread')
    t1 = threading.Thread(target=multiple_thread_function, args=('Samuel',3))
    t2 = threading.Thread(target=multiple_thread_function, args=('Maddie',2))
    t3 = threading.Thread(target=multiple_thread_function, args=('Jason',1))
    print('Main: before running the thread')

    t1.start()
    t2.start()
    t3.start()

    print('Main: wait for the thread to finish')
    t1.join()
    t2.join()
    t3.join()
    print('Main: all done!')

    """
    PROGRAM OUTPUT:

    Main    : before creating thread
    Main    : before running thread
    Thread "Samuel": starting
    Thread "Maddie": starting
    Thread "Jason": starting
    Main    : wait for the thread to finish
    Thread "Jason": finishing
    Thread "Maddie": finishing
    Thread "Samuel": finishing
    Main    : all done

    """
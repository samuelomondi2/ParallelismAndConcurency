
import threading

lock = threading.Lock()

def lock_threading_function(filename, count):
    # acquire the lock before entering the critical section
    # If another thread has the lock, this thread will wait
    # until it's released.
    lock.acquire()

    # Only 1 thread is running this code
    f = open(filename, 'w')
    f.write(count)
    f.close()

    # release the lock.  If you fail to release the lock,
    # the next thread that tried to acquire the lock will
    # wait forever since the release will never happen.
    lock.release()

if __name__ == '__main__':
    t = threading.Thread(target=lock_threading_function, args=('filename.txt', 3))

    t.start()
    t.join()
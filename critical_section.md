## Critical Sections

As a programmer you cannot control which thread runs on the cpu, or when the operating system will switch to another thread and for how long they will run when they have the CPU. This is only become a problem when you are running more than one thread. Take for example a code on writing and reading a file. 

| Thread A | Thread B |
|---|---|
| f = open(filename, 'w') |  |
| f.write(count) |  |
| OS switches to thread B ==> |  |
|  | f = open(filename, 'w') |
|  | Program crashes because the file is locked by thread A |

In the table above, Thread `B` will crash when trying to open the file in write only mode.  This is because Thread `A` never finished closing the file before Thread `B` started.

This is where **critical section** come into play. Python will allow you to denote part of your code as a critical section. A critical section in a sense is a code that only allows 1 thread to execute at a time. That thread will start and finish executing the code before any other thread can execute it. [Critical Section webpage](https://en.wikipedia.org/wiki/Critical_section)

To create a critical section, we will be using the Lock() method in the `threading module`. Calls to `acquire()` and `release()` need to match. If your code doesn't release a lock, then your program will hang on the next call to acquire(). This is called **Dead Lock**. [Lock code example](./locks_example.py)
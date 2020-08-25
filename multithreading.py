#----------------------------------
# threading module
# Timer object - run something after some amt of time has passed.
#----------------------------------
import threading
import time

def hello():
    print("hello, Timer")

if __name__ == '__main__':
    t = threading.Timer(3.0, hello)
    t.start()

#--------------------------------
# creating threads
#-------------------------------
import threading

def f():
    print("thread function")
    return
if __name__=='__main__':
    for ii in range(3):
        t = threading.Thread(target=f)
        t.start()
#------------------------------------------------------
# passing arguments to thrads to make thread more useful
#------------------------------------------------------
import threading

def f(id):
    print("thread function %s",%id)
    return
if __name__=='__main__':
    for ii in range(3):
        t = threading.Thread(target=f, args=(ii,))
        t.start()


#------------------------------------------------------
# identifying thread
#------------------------------------------------------
import threading
import time

def f1():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(1)
    print(threading.currentThread().getName(), 'Exiting')

def f2():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def f3():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='f2', target=f2)
t3 = threading.Thread(name='f3', target=f3)

t1.start()
t2.start()
t3.start()

# thttps://www.bogotobogo.com/python/Multithread/python_multithreading_Daemon_join_method_threads.php
# this website gives some good illustrations of how to use threading module..
# Also see the difference between threading and multiprocessing modules.



#----------------------------------
# logging module
#----------------------------------
import logging
logging.debug('This is a debug message') 
logging.info('This is an info message') 
logging.warning('This is a warning message') 
logging.error('This is an error message') 
logging.critical('This is a critical message')
# notice the printed output: the debug and info messgaes are not printed..

# that's because there's a level of seriousness set beyond which the messages should be printed.
# we can changes this as follows:
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message') 
logging.warning('This is a warning message') 
logging.error('This is an error message')  
logging.critical('This is a critical message')
# make sure that this basicConfig is set just after you freshly imported the module 'logging'.
# i.e make sure that non of the logging.{some_level}("") statement is called before setting basicConfig.
# because these logging.{some_level}("") say logging.debug("") implicitly set the basicConfig.
# and once basicConfig is set, it seems we can't change it again. (I haven't done very involved investigation of it.)

# output formatting1.
import logging 
logging.basicConfig(level=logging.DEBUG, format='%(process)d-%(asctime)s-%(levelname)s-%(message)s') 
logging.warning('Admin logged out.')

# output formatting2.
import logging 
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s-%(process)d-%(asctime)s-%(levelname)s-%(message)s', datefmt="%d-%b-%y %H:%M:%S")
#logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(process)d-%(asctime)s-%(levelname)s-%(message)s', datefmt="%d-%b-%y %H:%M:%S")
logging.warning('Admin logged out.')

# logging variable data 
import logging
name = 'John'
logging.error(f'{name} raised an error')

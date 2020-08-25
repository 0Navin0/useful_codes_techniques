from datetime import datetime, timedelta
#from threading import Timer, Thread  
import threading
import logging
#from time import time

# set logging format and loggigng level 
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(levelname)s-%(message)s')

def func(now,it):
    print("Iteration number %d, Some Task happening at %s"%(it,str(now)))

def f():
    return

def waiting_function(x):
    b=threading.Timer(x,f)
    b.setDaemon(True)
    return b
t1=time()
now = datetime.today()
delta_t = timedelta(seconds=10.0)
it = 0
#it_lim = int(input("give upper limit of iteration:")) 
it_lim = 10
while (it_lim-it):
    t=threading.Thread(target=func, args=(now,it))
    now+=delta_t
    if it<(it_lim-1):
        b=waiting_function(delta_t.total_seconds())
        t.start()
        b.start()
        t.join()
        b.join()
    else:
        t.start()
    it+=1
else:
    logging.debug('exited the loop.')
t2=time()
logging.debug('processing time:%f'%(t2-t1))

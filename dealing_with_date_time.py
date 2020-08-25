# if you spend enough time dealing with the properties of these objects, 
# eventually you will be able to apply these objects in your own custom made codes,
# with your own logic.

import time
from datetime import date
today = date.today()
# see the output format.
print(today,str(today),type(today))
print(date.fromisoformat('2020-02-20'))
# this is how again you can access the present date.
today == date.fromtimestamp(time.time())

# code to check number of days left before an event.
my_birthday = date(today.year, 5, 30)
if my_birthday < today:
    '''this inequality holds true if 'my_birthday' comes prior to 'today' in time.'''
    my_birthday = my_birthday.replace(year=today.year + 1)
    # this line makes sure that 'my_birthday' is always >= today....so that 
    # the number left from the 'time_to_birthday' always specifies the upcoming birthday.   
print(my_birthday)
time_to_birthday = abs(my_birthday - today)
# This abs is not needed.

print(time_to_birthday.days)
if time_to_birthday.seconds == 0:
    print("Happy Birthday!\t:)"

# storing date in a variable
string= str(date.today()) # = today.isoformat() # also know today.isoweekday()

# modifying a date type of object....like 'today')
# this code needs attention to cover all the cases of 30/31 day a month
new_date = today.replace(year=today.year+1, month=(today.month+1)%13, day=today.day+1)
# date.today.replace() has only 3 keyword arguments; year,month,day; I can't set a time into it.

from datetime import datetime
x = datetime.today()
# datetime.today() contains both date and time. and we can manipulate both by replace option... 
# so it looks better than date.today.replace()
print(x)
#print(str(x.time())) # prints time when the variable was defined.
#print(str(x.today())) # prints current machine time.
#print(str(x.day())) # prints day when the variable was defined.
y = x.replace(day = x.day+1, hour=1, minute=0, second=0, microsecond=0)

#---------------------------------------------------------------------------
# code to run a specific code at a given time(here after 10 seconds) once:
#---------------------------------------------------------------------------
from datetime import datetime
from threading import Timer

def func():
    print("Some Task")

x = datetime.today()
y = x.replace(second=x.second+10)
delta_t = y-x
secds = delta_t.total_seconds()
t = Timer(secds, func)
t.start()

# within the 'delay period' given inside Timer(), we can cancel the work to be done
# by Timer() by using- 
#t.cancel() 

#-----------------------------------------------------------------------
# code to run a specific code repeatedly after a certain time imterval
#-----------------------------------------------------------------------
# this code successfully makes the while loop run with required time delays.
# there doen't appear to be any memory issue, since iterations don't store anything.

from datetime import datetime, timedelta
from time import sleep, time
import logging

# set logging format and loggigng level
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(levelname)s-%(message)s')

def func(now,it): 
    print("Iteration number %d, Some Task happening at %s"%(it,str(now)))

def waiting_function(x,y):
    y+=1
    # to sleep only 4 times
    if y>4:
        y=False
        logging.debug('exiting the loop.')
        return y 
    # waiting for next event.
    else:           
        sleep(x)
        return y

t1=time()        
now = datetime.today() 
delta_t = timedelta(seconds=10.0) 
condition = 1
while condition:
    func(now,condition)
    now = now + delta_t
    # setting up wait time for next iteration
    condition = waiting_function(delta_t.total_seconds(),condition)
t2=time()

print(t2-t1)
logging.debug('extra processing time %f'%(t2-t1))
#--------------------------------------------------------------------------------------

from datetime import datetime, timedelta 
#from threading import Timer, Thread 
import threading
from time import time 
import logging

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
it = 1 
#it_lim = int(input("give upper limit of iteration:")) 
it_lim = 10
while it: 
    if it > it_lim:           
        it=False 
        logging.debug('Exiting the loop.') 
    else: 
        t=threading.Thread(target=func, args=(now,it)) 
        now+=delta_t 
        if it<it_lim: 
            b=waiting_function(delta_t.total_seconds()) 
            t.start() 
            b.start() 
            t.join() 
            b.join() 
        else: 
            t.start() 
        it+=1
t2=time()

print(t2-t1)
logging.debug('extra processing time %f'%(t2-t1))

#--------------------------------------------------------------------------------------
from datetime import datetime, timedelta 
#from threading import Timer, Thread  
import threading 
import logging  
from time import time 
 
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

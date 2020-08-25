## using MPI module
##************************
from mpi4py import MPI
import numpy as np
from astropy.io import fits
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
if rank == 0:
    # Read SQL query results
    with fits.open('/home/navin/Downloads/wget/32210.fits') as SQLquery:
         sql_data = SQLquery[1].data

    # Get all unique tracts
    tracts = np.sort(np.unique(sql_data['tract']))
    data = np.array([1,2,3])
    print('data processed in rank %d, and will be sent to all processros including itself.'%rank)
else:
    tracts = None
    data = None
tracts = comm.bcast(tracts, root=0)
data = comm.bcast(data, root=0)
print('rank=%d'%rank, len(tracts), ',another data',data) 
#if rank ==1:
#    '''notice that if we try to receive the same information from the sender processor twice, the second time, the recieving processor
#will not get the information because, if once the data is recieved, it got used up and it was moved from sender processors memory location.
#so the receiving processor will keep on waiting until you do a keyboard interrupt.''' 
#    tracts_copy = comm.recv(source=0)
#    print('tracts copy',tracts_copy)

'''Also check out the use of scattering and gathering in this module.'''

##******************************************
## Using concurrent module       https://www.youtube.com/watch?v=fKl2JW_qrso 
##******************************************
import time
import concurrent
def do_sth(sec): 
    print(f'sleeping {sec} seconds...') 
    time.sleep(sec) 
    return(f'done sleeping {sec} seconds...') 
    
# You see that all the 12 codes are mapped to the function at the same time...parallelized!
# You can say so looking at the print statements.
with concurrent.futures.ProcessPoolExecutor() as executor: 
    secs=[12,11,10,9,8,7,6,5,4,3,2,1] 
    results = executor.map(do_sth,secs) 
    for result in results: 
        print(result) 
# exector.map() maps all the inputs to the function at the same time but outputs the resluts in the order of input.
# this behavior can be very useful...I used it to do some operation on an array input and then finally extracting the resulting array as one object
# by assigning the values into an empty array of the relevant size.
# if all the 12 inputs print at the same time, that means first 12 inputs are paraleeized into 12 threads of the 6 cores...what if I give 13 inputs?
with concurrent.futures.ProcessPoolExecutor() as executor: 
    secs=[13,12,11,10,9,8,7,6,5,4,3,2,1] 
    results = executor.map(do_sth,secs) 
    for result in results: 
        print(result) 
# you should see the last input gets assigned for execution a bit later.

## Using this module, it's very easy to do threading(pooling of threads) or multiprocessing(pooling  of processes).

#--------------------------------------------------------------------------------
# assigning multiple arguments to a function being paralellized in this code:
#--------------------------------------------------------------------------------
import numpy as np
x=np.arange(1,11,1)
y=np.arange(1,11,1)
z=np.arange(1,11,1)
def f(x,y,z,do=False):
    """a function with multiple positional arguments and a keyword argument.""" 
    if do==True: 
        return z**2+x+2*y 
    else: 
        return x

with concurrent.futures.ProcessPoolExecutor() as executor: 
    results = executor.map(f,*[x,y,z,[True for ii in range(x.size)]]) 
#    map supplied same index values from all the arrays/lists into the funciton at once. 
    i = np.zeros(x.size)
    for o,result in enumerate(results): 
        i[o] = result
        print(f"{o}--->{type(result)}")

#with concurrent.futures.ProcessPoolExecutor() as executor: 
#    results = executor.map(f,*[x,y,z,[True for ii in range(x.size-1)]+[False]]) 
##    map supplied same index values from all the arrays/lists into the funciton at once. 
#    i = np.zeros(x.size)
#    for o,result in enumerate(results): 
#        i[o] = result
#        print(f"{o}--->{type(result)}")
#
#with concurrent.futures.ProcessPoolExecutor() as executor: 
#    results = executor.map(f,*[x,y,z,[False for ii in range(x.size)]]) 
#    map supplied same index values from all the arrays/lists into the funciton at once. 
#    i = np.zeros(x.size)
#    for o,result in enumerate(results): 
#        i[o] = result
#        print(f"{o}--->{type(result)}")

#-----------------------------------------------------
# using executor.submit() and as_completed()
# to get the result of a function execution in the order it gets completed.
#------------------------------------------------------
def t(a,b,c):
    print(a,b,c)

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(t,a,b,c) for a,b,c in zip(np.arange(1,10,1),repeat([10]),repeat(0))]  
for f in concurrent.futures.as_completed(futures):
    print(f.result())
# you can see the order in which the values are printed is different from the order in which they were submitted.



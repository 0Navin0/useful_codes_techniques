##collections: used defaultdict, dicttionary.items(), string.join()
##itertools: repeat
## map,
from collections import defaultdict

#defaultdict can be used to do various things like:
## 1) frequency count of many different keywords...all at once.
## this was used inside the ZTF code https://github.com/0Navin0/ztf-avro-alert/blob/master/notebooks/Filtering_alerts.ipynb
d= "spam "
d=d*5 + 'killer' + ' funky' + ' robo' + ' tom' + ' funky' + ' robo'
print(d)
d=d.split(' ')
print(d)
# notice: int function defaults to value=0;
count = defaultdict(int)
# inside defaultdict we need to specify a function so that if some key 
# is not found inside the dictionary 'count', then a new key will be created to
# which a default value will be assigned by this function.
for name in d:
    count[name]+=1
print(count)

## 2) creating a dictionary of default list type elemtns and then collecting all the cities in a given state.
city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), 
('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)
# check out the defaultdict format----first it shows the default function and then the dictionary itself.
print(cities_by_state)

for state,city in city_list:
    cities_by_state[state].append(city)
# check out the usefulness of items().....it converted the dict into list of tuples...over which we can iterate.
for state,cities in cities_by_state.items():
    print(state,', '.join(cities))


## use of str.join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#------------------------------------------------------
from itertools import repeat
import numpy as np

print(repeat(10,10)) #it acts as a generator(an iterator...all interators are iterables..but not all iterables are iterators.)
print(list(repeat(10,10))) #second argument tells how many times should the first argument be generated....if second arg is absent...it gives an infinite generator.
# but generators don't keep the memory occupied unlike lists(or other containers/interables) rather, they just access on element at a time.
#after the values of the generator are exhausted, asking for 'next' value from it by 'next(generator)' will cause a 'StopIteration' exception.
def f(a,arr): 
    try: 
        while True: 
            print(next(a)) 
            print('This printed array {}'.format(next(arr))) 
    except StopIteration: 
        print('Iterator exhausted') 
    return 'done!'
arr = np.arange(1,10,1)

print(f(repeat(10,10),repeat(arr)))
#------------------------------------------------------
def g(a,b):
    print(f'a={type(a)},\tb={type(b)}') # check the type of object passed on throught a repeat object.
    return a,b # this is a tuple.

o=map(g,repeat(np.arange(1,10,1),10),enumerate(repeat(1,10))) #map and repeat are very useful tools...you can pass any object into a function using map...and you can 
p=map(g,[i for i in range(1,11)],repeat([1],10))
for ii in o:
    print(ii)
for ii in p:
    print(ii)

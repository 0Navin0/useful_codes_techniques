# supplying arguments within firt integral

from scipy.integrate import quad
import numpy as np

def integrand(x, a, b):
    return a*x**2 + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)

#-----------------------------------
# limits can be infinite too in (quad), 
# vetorizing the input to an integral, 
# double integrals from repeated use of quad...without using dblquad.
#-----------------------------------
def integrand(t, n, x):
    return np.exp(-x*t) / t**n


def expint(n, x):
    return quad(integrand, 1, np.inf, args=(n, x))[0]

vec_expint = np.vectorize(expint)
vec_expint(3, np.arange(1.0, 4.0, 0.5))

result = quad(lambda x: expint(3, x), 0, np.inf) 
# in using quad there can be only one variable.
pirnt(result)

#----------------------------------------------------------------------
# np.vectorize() is a nice convenient function...note it's a conveniennce funcion and  not a performance function.
#----------------------------------------------------------------------
def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b
    else:
        return a + b

vfunc = np.vectorize(myfunc)
vfunc([1, 2, 3, 4], 2)

#-----------------------------------
# dblquad, tplqual and nquad
#-----------------------------------
# in using multiple integration functions...the limits of all integrals are to be defined as function
# below example: inner integ from (1,inf), outer integ from (0,inf), limits are constants.

from scipy.integrate import quad, dblquad
def I(n):
    return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)

# for veriable inner limits:
from scipy.integrate import dblquad
area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)

""" 
The integration bounds are an iterable object: either a list of constant bounds, 
or a list of functions for the non-constant integration bounds. The order of integration 
(and therefore the bounds) is from the innermost integral to the outermost one.
"""
# nquad:
from scipy import integrate
N = 5
def f(t, x):
   return np.exp(-x*t) / t**N

integrate.nquad(f, [[1, np.inf],[0, np.inf]])

# order on integ: inner integration is over t from [1, np.inf] and outer is on x variable from [0, np.inf].
# Notice, limits of integ are constants and supplied as an iterable...following the order of integration.
# for variable inner limits of integ, the iterable has to be an interable of functions as follows:

from scipy import integrate
def f(x, y):
    return x*y

def bounds_y():
    return [0, 0.5]

def bounds_x(y): # Notice: the variable bounds ...that means this is the inner integration variable.
    return [0, 1-2*y]

integrate.nquad(f, [bounds_x, bounds_y])

# nth order derivative w.r.t to one variable using central point formula.

# there's an argument to decide whether we use 3 point or 5 point..and so on.
# you can also supply arguments to the function being differentiated..
# it's possible to write a code to get partial derivatives too.

from scipy.misc import derivative
def f(x):
    return x**3 + x**2
derivative(f, 1.0, dx=1e-6)

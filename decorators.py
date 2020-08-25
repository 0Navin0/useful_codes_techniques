# summary of topics covered: 
    ''' closures in python
        decorator functions
        decorator class
    '''

'''
step: 1 
'''
def outer_function():
    # local variable of outer_function==message
    message = 'Hi'

    def inner_function():
        # message variable is accessible to the inner_function but wasn't created within it...
        # called free variable for inner_function
        print(message)
    return inner_function()

print(outer_function)
'''
step: 2 
'''
def outer_function():
    # local variable of outer_function==message
    message = 'Hi'

    def inner_function():
        # message variable is accessible to the inner_function but wasn't created within it...
        # called free variable for inner_function
        print(message)
    return inner_function

# now, my_func==inner_function with a free parameter 'message',waiting to be exectued. 
my_func = outer_function()
my_func()
my_func()
my_func()
my_func()
my_func()
my_func()
# so the inner function remembers the state of free variable even when the inner_function has finished executing.
'''
step: 3 
'''
def outer_function(msg):
    # local variable of outer_function==message
    message = msg

    def inner_function():
        # message variable is accessible to the inner_function but wasn't created within it...
        # called free variable for inner_function
        print(message)
    return inner_function()

hi_func = outer_function('hi')
Bye_func = outer_function('bye')
'''
step: 4
'''
def outer_function(msg):
    def inner_function():
        # message variable is accessible to the inner_function but wasn't created within it...
        # called free variable for inner_function
        print(msg)
    return inner_function()

hi_func = outer_function('hi')
Bye_func = outer_function('bye')

#----------------------------------------------------------------

''' 
decorator: a function that takes as an argument another function and 
adds some extra functionality to the function taken as input without 
altering the code of the input function.
'''

'''
step 1
'''

def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function
'''
the decorator_function is just like the closures we discussed above,
what does it do? :
it returns the wrapper_function which is waiting to be executed
'''

'''
step 2
'''
# simplest example of a decorator:
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran.')

decorated_display = decorator_function(display)
# decorated_display is the wrapper function which is waiting to be exectud.
# and when the wrapper function runs, it just executes the original_function that we passed in.

decorated_display()

# check out what this prints;
decorated_display

'''
step 3
'''

def decorator_function(original_function):
    print('decorator_function ran.')
    def wrapper_function():
        print('wrapper_function executed this before {}.'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran.')

# what happens if we do this?
display = decorator_function(display)
display()
# display.__name__ 

# what happens if we do this in continuation with the above two lines?
display = decorator_function(display)
display()
# so once, in here, we're feeding the wrapper_function to the decorator_function..rest you can imagine.

'''
Notice: doing this once: display = decorator_function(display)
is same as using the following syntax in python.
'''

@decorator_function
def display():
    print('display function ran.')

display()

'''
step 4
'''
# what if our original_function had to have arguments in it?
# will the above snippet of code work?

def decorator_function(original_function):
    print('decorator_function ran.')
    def wrapper_function():
        print('wrapper_function executed this before {}.'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments {} & {}.'.format(name, age))

# running the following will give error
display_info('Me',26)

'''
step 5
'''
# corrected to accept any numbre of positional and keyword arguments:

def decorator_function(original_function):
    print('decorator_function ran.')
    def wrapper_function(*args, **kwargs):
        print('wrapper_function executed this before {}.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments {} & {}.'.format(name, age))

# No error
display_info('Me',26)


'''
step 6
'''
class decorator_class:
    
    def __init__(self, original_function):
        self.original_function = original_function
    # doing this tied our original function the class instance.

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments {} & {}.'.format(name, age))

# No error
display_info('Me',26)































def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print("display function run")

decorated_display = decorator_function(display)
decorated_display()

################################
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper function execte before original function name {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print("display function run")

decorated_display = decorator_function(display)
decorated_display()

#######################################
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper function execte before original function name {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("display function run")

display()

#########################################
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper function execte before original function name {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function run")

@decorator_function
def display_info(name,age):
    print("name is: {} and age is: {}".format(name,age))

#display()
display_info("john",25)

#########################################
class decorator_class(object):

    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self,*args,**kwargs):
        print('call method executed before original function name {}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorator_class
def display():
    print("display function run")

@decorator_class
def display_info(name,age):
    print("name is: {} and age is: {}".format(name,age))

display()
display_info("john",25)

#########################################

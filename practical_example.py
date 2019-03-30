#practical example of decorators
#logging to keep track how many time a specific function run with passed arguments
from functools import wraps

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args,**kwargs):
        logging.info('Ran with args: {} and kwargs: {}'.format(args,kwargs))
        return original_function(*args,**kwargs)
    return wrapper

def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = original_function(*args,**kwargs)
        timeDiff = time.time() - t1
        print('function name {} ran in sec {}'.format(original_function.__name__,timeDiff))
        return result
    return wrapper
   
'''
@my_logger
def display():
    print("display function run")
'''

import time

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print("name is: {} and age is: {}".format(name,age))

display_info = my_logger(my_timer(display_info))
                                                   
display_info("Tom",22)


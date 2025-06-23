#Today I am learning very new topic, whose name i never heard when I was learning python in college, and the name of the topic is Decorators, I understand that Functions are the first class objects in python. What I mean here is that they can be treated as a variable and one can pass them as an arguments to another function, or even return them as a return value.

import time
def timer_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        duration_sec = end-start
        print(f'{func.__name__} took {duration_sec} to execute')
    return wrapper


@timer_it
def multiply(number):
    print(f'running multiply function')
    for x in number:
        for y in number:
            for z in number:
                x*y*z

@timer_it
def addition(number):
    print(f'running addition function')
    for x in number:
        for y in number:
            for z in number:
                x+y+z
    
multiply(range(1,100))
addition(range(1,100))
    

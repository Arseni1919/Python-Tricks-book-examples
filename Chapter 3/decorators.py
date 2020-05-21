def null_decorator(func):
    return func

import functools # for debugging - makes all inside methods immigrate to a new function
                 # like __name__ and so on

def uppercase(func):
    @functools.wraps(func)
    def wrapper(a):
        original_result = func() + a
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def strong(func):
    @functools.wraps(func)
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def proxy(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
        f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
        f'returned {original_result!r}')

        return original_result
    return wrapper


@uppercase
@strong
@emphasis
def greet():
    return f'Hello!'

@trace
def say(name, line):
    return f'{name}: {line}'

a = ""
print(greet(a))
print(say('Jane', 'Hello, World'))

decorated_greet = strong(emphasis(greet))
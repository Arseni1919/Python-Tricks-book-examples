import functools # for debugging - makes all inside methods immigrate to a new function
                 # like __name__ and so on

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo('hello', 1, 2, 3, key1='value', key2=999)

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function
@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)

greet('Hello', 'Bob')

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

genexpr = (x * x for x in range(3))
print_vector(*genexpr)

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)
print_vector(*dict_vec)
#generator
def repeater(value):
    while True:
        yield value

iterator = repeater('Hi')
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for x in repeater('Hi'):
#     print(x)

def repeat_three_times(value):
    yield value
    yield value
    yield value

for x in repeat_three_times('Hey there'):
    print(x)


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

for x in bounded_repeater('Hi', 4):
    print(x)

# and the shortest one
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

# genexpr = (expression for item in collection)
# =============================================
# def generator():
#     for item in collection:
#         yield expression
genexpr = ('Hello' for i in range(3))

print(genexpr) # generator object

# genexpr = (expression for item in collection if condition)
# ==========================================================
# def generator():
#     for item in collection:
#         if condition:
#             yield expression
even_squares = (x * x for x in range(10) if x % 2 == 0)

print(even_squares) # generator object

for x in ('Bom dia' for i in range(3)):
    print(x)

sum(x * 2 for x in range(10))

# very efficient one value at each time
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)

print(list(negated))
print(list(negated)) # can not to use the same generator twice
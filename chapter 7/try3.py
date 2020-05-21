print({True: 'yes', 1: 'no', 1.0: 'maybe'})
print({False: 'yes', 0: 'no', 0.0: 'maybe'})
# -------------------------------------------------------------

xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}
zs = {}
zs.update(xs)
zs.update(ys)
print(zs)
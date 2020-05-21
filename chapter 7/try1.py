name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}
def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')

print(greeting(382))
print(greeting(000))

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items()))
print(sorted(xs.items(), key=lambda x: x[1]))
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
print(sorted(xs.items(), key=lambda x: x[1], reverse=True))
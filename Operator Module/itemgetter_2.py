from operator import itemgetter

List = ['a','b','c','d']

Ig = itemgetter(2)(List)
print(Ig)

print()

Tuple = ('a','b','c','d')

Ig = itemgetter(1)(Tuple)
print(Ig)
print()

Dict = {'a':1,'b':2}
Ig = itemgetter('b')(Dict)
print(Ig)

# getsizeof() return the size of an object in bytes

from sys import getsizeof

a = (1,2,3,4)
b = [1,2,3,4]
c = {1,2,3,4}
d = {'a':1,'b':2,'c':3,'d':4}

print('Tuple size',a)
print(getsizeof(a))

print('List size',b)
print(getsizeof(b))

print('Set size',c)
print(getsizeof(c))

print('Dict size',d)
print(getsizeof(d))
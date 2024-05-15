
# lambda value:expressen
# specifie the expressen which mean close the expression into
# into following 
# dict {express},tuple(expression),list[expression]

Dict = lambda key,value:({key:value})
print(Dict('a',1))
print()

Tuple = lambda m,n:(m+n,)
print(Tuple(2,3))
print()

List = lambda m,n:[m+n,m-n]
print(List(4,2))

keys = ['a','b','c','d']
values = [1,2,3,4]

Dict = dict(map(lambda k,v:(k,v),keys,values)) 
# return tuple which is also mapping object
print(Dict)
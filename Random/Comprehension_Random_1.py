from random import randint # from randum module only import randint method
from array import array # import only array method

List = [randint(1,10) for u in range(1,10)]
print(List)

Tuple =tuple((randint(1,10) for u in range(1,10)))
print(Tuple)


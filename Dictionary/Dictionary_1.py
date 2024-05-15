# -------------Dictionary
# A Dictionary represents a group of elements in the form
# of key value pairs.Dictionary in Python is an unorderd collaction.
# Dictionries are mutable so we can modify it's item without changing
# their identity. Dictionaries are represented using curly braket {}
# Eyntax:--
# 		Dictionary_Name={key1:value1,key2:value2,....}
# 		keys are case sensitive
#       keys cann't be repeated
#  		keys must be immutabel  for instance  Integers, String,tuple,
# if we mention same key again,the old key will be overwritten.

# creating  A Dictionary Various ways

Dict = {1:"one",2:"two",3:"three"}
print(Dict)
print("\na==b==c==d==e==f")
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict((['two', 2], ['one', 1],['three', 3]))
print(a == b == c == d == e==f)

En = dict(enumerate(['a','b','c'],start=1))
print(En)
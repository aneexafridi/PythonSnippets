# Question_1
# sort (ascending and descending) a Dictionary
# by values

Dict = {'a':4,'c':2,'b':3,'d':1}
print(Dict)
print("Ascending order the values of Dictionary")
print(sorted(Dict.values()))
# we can convert into tuple or list Dict.keys
print("Descending order the values of Dictionary")
# first step sort the values then reversed then convert into list
print(list(reversed(sorted(Dict.values()))))
# The same logic is valid for keys of dictionary
# --------------sum(iterable, /, start=0)
# Sums start and the items of an iterable
# from left to right and returns the total. 
# The iterable’s items are normally numbers,
# and the start value is not allowed
# to be a string.
# Syntax:
#       Sum(iterable_object_Name)
Dict = {1:11,2:22,3:33}
print(Dict)
print("Sum of keys: ",sum(Dict.keys()))
print("Sum of Values: ",sum(Dict.values()))
Tuple = (1,2,3)
print(Tuple)
print("Sum of Tuple",sum(Tuple))
List = [1,3,5]
print(List)
print("Sum of List",sum(List))
Set = {4,5,6}
print(Set)
print("Sum of Set",sum(Set))
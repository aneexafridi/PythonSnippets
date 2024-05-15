# ---------map() Function
# This fucntion executes a specified function on each element
# of the iterable (sequance) and perhaps changes the elements.
# Syntax:- 
# 		map(Function_Name,iterable_object_Name)
# Function_Name = It's name of a function which perform an operation
# on all the elements of the sequance and modified elements are
# returned which can be stored in another sequance.

# Iterable   ---- Iterable may be either a sequance, list,string,tuple
# which supports iteration, or an iterator.

List_1 = [1,2,3,4]
List_2 = [11,21,31,41]
print(List_1)
print(List_2)
result = list(map(lambda x,y:x+y,List_1,List_2))
print(type(result))
print(result)
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

List = [1,2,3,4]
print(List)
def Increment(List_data):
	return List_data+10

result = tuple(map(Increment,List))
print(result)
print(type(result))
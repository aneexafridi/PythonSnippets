# filter() Method
# the filter functiion is used to filter out the elements
# of an iterable (sequence) depending on a function that
# tests each element in the sequence to be true or not
# It returns those elements of sequence, for while function is true.
# Syntax:- 
# 	filter(Function_Name,iterable_object_Name)

# Function_Name -- It's name of a function which tests each
# element in the sequence return True or False.
# If function_Name is None, returns the elements that are True.
# iterable object = String list,tuple,dict,etc

List = [11,22,33,44,55]
print(List)
# we can store as list() the filter method return
result = list(filter(lambda n: (n%2==0),List))
print(type(result))
print(result)
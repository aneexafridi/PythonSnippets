# this method is used to remove specified
# by position number, from the existing Array
# and returns removed element

# Syntax:- Array_Name.pop(position)

from array import *
Array = array('i',[1,2,3,4,5])
print(Array)
print("After Pop the Element from the Array")
Return_element = Array.pop(2)
print(Return_element)
print(Array)
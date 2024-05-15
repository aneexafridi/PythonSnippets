# This method is used to remove
# first occurrence of given element from the
# existing array.If it does not found the element,
# shows valueError

from array import *
Array = array('i',[1,2,3,4,5])
print(Array)
print("After Remove the Element from the Array")
Array.remove(3)
print(Array) 
# The Method is used to append another
# array or iterable object at the end
# of Array
# Syntax:-- 
# 			Array_Name.extend(another_Array)

from array import*
Array_1 = array("i",[1,2,3,4,5])
print(Array_1)
print("After extend the another Array")
Array_2 = array('i',[6,7,8,9,10])
Array_1.extend(Array_2)
print(Array_1)
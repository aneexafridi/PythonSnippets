# array() Function
# Syntax:-  Name_Array = array([elements])
from numpy import*
Array_int = array([1,2,3,4,5])
print(Array_int)
Array_str = array(["Shahab","Afridi","Fawad","Afridi"])
print(Array_str)
Array_chr = array(['A','B','c','d'])
print(Array_chr)
Array_chr[0] = "Z" # change the value and return to Array
print(Array_chr)
print("Length of Array_int",len(Array_int))
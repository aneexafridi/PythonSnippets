#----------------tolist() Method
# this method convert Array into List
# Syntax: 
#		Array_Name.tolist()
from array import *

Array = array('i',[1,2,3,4])
print(Array)
print(type(Array))
print("After convert the Array into List")
To_List = Array.tolist()
print(To_List)
print(type(To_List))
# Slicing on Array can be used to retrieve a piece
# of the array that contains a group of 
# elements. Slicing is useful to retrieve a range
# of elements.
# Syntax:- Array_Name[start:stop:step]
# and also return

# --------------Note --------
#     [x::y]  in this case compiler set the
# default end length of the Sequence
from array import*
Array_1 = array('i',[1,2,3,4,5])
print(Array_1[1:4])
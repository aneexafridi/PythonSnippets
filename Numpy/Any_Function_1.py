# any() Function
# this function returns True,if any one element of the
# iterable is True. If iterable is empty then returns False.
# --- Note--any() this is Python's built-n function
from numpy import *
Araray_A = array([1,2,3,4])
Araray_B = array([5,6,7,8])
# same Array_C = (Array_A==Array_B)  then any(Array_C)
print(any(Araray_A==Araray_B))
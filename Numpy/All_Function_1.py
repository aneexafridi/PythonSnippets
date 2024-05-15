# All() Function
# this function returns True,If all  elements of the
# iterables are True or iterable is empty ortherwise False
# --- Note--all() this is Python's built-n function
from numpy import *
Array_A = array([1,2,3,4])
Array_B = array([5,6,7,8])
# same Array_C = (Array_A==Array_B)  then all(Array_C)
print(all(Array_A==Array_B))
Array_A = array([1,2,3,4])
Array_B = array([1,2,3,4])
print(all(Array_A==Array_B))
Array_A = array([]) # empty
Array_B = array([])
print(all(Array_A==Array_B))
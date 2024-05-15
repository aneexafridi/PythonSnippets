# -----------------reversed(seq)
# Return a reverse iterator. 
# seq must be an object which has a __reversed__() method
# or supports the sequence protocol (the __len__() method
# and the __getitem__() method with integer 
# arguments starting at 0).
# ------------Note----------
# when we are using "reversed()" method 
# must be convert the type i.e  list,tuple
List = [1,2,3]
print("List: ",list(reversed(List)))
Tuple = (1,2,3)
print("Tuple: ",tuple(reversed(Tuple)))
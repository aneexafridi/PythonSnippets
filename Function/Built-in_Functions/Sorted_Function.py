# ----------------sorted() method
# this method return a new list with sorted data
# --------------Note
# sorted() method work only same data type in 
# itrable object like (1,2,3) ,("a","h","g") and
#  and also  max() and min()
#  ############## ->>>>> help(sorted)

Tuple = (3,1,2)
print(Tuple)
print("The Sort Data: ",sorted(Tuple))
print(type(Tuple))

String = "Equal"
print(sorted(String))
print(sorted((5,3)))
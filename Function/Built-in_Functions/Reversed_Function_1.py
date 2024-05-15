# -----------------reversed() Method
# this method return that datatype which is use
# for example list,tuple ete.
# Syntax:
# 		list(reversed(list_name))
# 		tuple(reversed(tuple_Name))

# use help(reversed)
List = [1,2,3]
print("List: ",list(reversed(List)))
Tuple = (1,2,3)
print("Tuple: ",tuple(reversed(Tuple)))

# Note---------------------reverse VS reversed
# reverse is the method of list class and only use for list object
# reversed is the built-in function  which can be use at iterable object

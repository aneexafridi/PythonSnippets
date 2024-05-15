# ---------------Tuple
# Tuple contain a group of elements  which can be same or Differnt types
# Tuple are used to store data which should not be modified.
# It occupies less memory compare to list
# Tuples are immutable.
# Examples:--- 						------Note-----
									# T = (1)  not Tuple and same T = 1
									# T = (1,) Tuple with one Element
# 	Tuple = () Empty Tuple Create  
# 	Tuple_1 = (1,3,4,"Equal",'A')
# 	Tuple_2 = 1,2,3,"Equal",'A'
# 	Tuple_1 and Tuple_2 are Same
# 	without parenthese will be work
#   Access by index []
Tuple_1 = () # create Empty Tuple
print(Tuple_1)

Tuple_2 = (1,2,3,4,"Equa",'A')
print(Tuple_2)

t = 2, # Not same as t=2 
print(t)
print(type(t))
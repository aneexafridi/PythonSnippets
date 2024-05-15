# help(map)
# Tuple_1 is string tuple
# Tuple_2 is int tuple
# To add string and integer we should convert
# integer into string then we can add

Tuple_1 = ('a','b','c')
Tuple_2 = (1,2,3)
print(list(map(lambda x,y:x+str(y),Tuple_1,Tuple_2)))
# x corresponding for Tuple_1
# y corresponding for Tuple_2
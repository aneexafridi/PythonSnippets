# # help(map)

Tuple_1 = [1,2,3,4,5]
Tuple_2 = [10,20,30,40,50]

print(tuple(map(lambda a,b:a+b,Tuple_1,Tuple_2)))

# if we give the size of two list/tuple doesn't same
# the return the short list/tuple corresponding element

List_1 = [1,2,3]
List_2 = [11,22,33,44]
print()
print(list(map(lambda x,y:x+y,List_1,List_2)))








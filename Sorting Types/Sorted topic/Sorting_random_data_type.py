# for multiple data type in iterable object
# Note-------
# like ,list,tuple,string,set,etc
# then we should use the
# sorted Function with parameter key
# Note ->>> 
#     key=str --> commonly use
#	  key=repr--> commonly use
#     key=len---> commonly use
# 	  key=bool
# 	  key=ascii
# 	  key=hash
#     key=id
#-----------------------------------------------
# all built-in functions
# all return specific comparison there functions


List = [4,1,'c',2.5,'a',True,'3','b',False]
# List = "41c2.5aTrue3bFalse"
print(List)
print('After sorting')

# List.sort(key=str) only for list defined
# print(List)
Sorted_list = sorted(List,key=str)
print(Sorted_list)
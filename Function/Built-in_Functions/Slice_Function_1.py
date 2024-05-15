# 			Slice built-in Funciton


List = ['A','B','C','D']
print(List)
print(List[slice(0,9)]) # print 0 to all
print(List[slice(2,8)]) # print 2 to all

# if we put List[9] which is outof index Error Raise
# but in slice handle it,
print(List[slice(-1)])

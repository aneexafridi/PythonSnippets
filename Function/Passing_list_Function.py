def Show_List_R(List_Data):
	print(type(List_Data))
	return List_Data

def Show_List(List_Data):
	print(type(List_Data))
	print(List_Data)

List = [1,2,3,4,"Equal"]

Show_List(List)
print(Show_List_R(List)) # return list method here call

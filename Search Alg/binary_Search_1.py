# binary search only apply sequence iterable mean
# List=[1,4,5,6,9,10]

List = [1,4,5,6,9,13]

Element = 13

Lower_Boundry = 0
Upper_Boundry = len(List)-1

while Lower_Boundry<Upper_Boundry:
	Middle = (Lower_Boundry+Upper_Boundry)//2
	if List[Middle] < Element:
		Lower_Boundry = Middle + 1
	else:
		Upper_Boundry = Middle

if Element == List[Lower_Boundry]:
	print("Index: ",Lower_Boundry)
else:
	print("Not Exit")






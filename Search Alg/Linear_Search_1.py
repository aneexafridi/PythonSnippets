						  # Linear Search
List = [4,1,6,2,9,3]

Element = 9

Lower_Boundry = 0
Upper_Boundry = len(List)-1
Success = False

while Lower_Boundry<=Upper_Boundry:
	if List[Lower_Boundry] == Element:
		print('Index: ',Lower_Boundry)
		Success = True
		break
	else:
		Lower_Boundry+=1

if Success is True:
	print(List[Lower_Boundry])
else:
	print("Not Exist")







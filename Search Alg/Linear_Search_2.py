						  # Linear Search

def Linear_Search(List,Element):
	Lower_Boundry = 0
	Upper_Boundry = len(List)-1
	Location = 0
	while Lower_Boundry<=Upper_Boundry and List[Lower_Boundry] != Element:
		Lower_Boundry+=1
	if Lower_Boundry<=Upper_Boundry:
		Location = Lower_Boundry+1
	
	return Location


List = [4,1,6,2,9,3]

Element = 4

print(Linear_Search(List,Element))
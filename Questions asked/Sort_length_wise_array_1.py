# write a function that take an array of strings
# as argument and returns sorted array
# containing the same strings,ordered from shortest to longest
# for example
# 				['Telescope','Glasses','Eyes','Monocles']
# function would return like
#	  			['Eyes','Glasses','Monocles','Telescope']

List = ['Telescope','Glasses','Eyes','Monocles']

def Sorting(List):
	return sorted(List,key=lambda x:len(x))

print(Sorting(List))	

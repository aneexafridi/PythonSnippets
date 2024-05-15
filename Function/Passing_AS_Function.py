def MyFunction(myfun):
	print("My Function\n"+myfun)# myfun() can use
def YourFunction():
	return "your Function"

MyFunction(YourFunction()) # YourFunction can use
# both comment use then work
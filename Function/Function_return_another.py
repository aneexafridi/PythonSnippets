def MyFunction():
	def YourFunction():
		return "Your Function"
	print("My Function")
	return YourFunction()
print(MyFunction())

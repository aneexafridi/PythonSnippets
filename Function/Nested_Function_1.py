def OuterFunction():
	print("Outer Function")
	def InnerFunction():
		print("Inner Function")
	InnerFunction() # call inner function

OuterFunction()
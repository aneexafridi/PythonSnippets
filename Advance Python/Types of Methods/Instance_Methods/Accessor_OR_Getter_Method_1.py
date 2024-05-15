# ------------------Accessor Method
# This method is used to access or read data of the variables.
# This method do not modify the data in the variable.
# This is also called as getter Method.
# Ex:---
# 		def get_Name(self):
# 		def get_Age(self):
# 		def get_Roll(self):

class Person:
	def __init__(self): # special method or Constractor
		self.Name = "Equal" # Instance variable
	def get_Name(self):  # accessor method
		return self.Name
		
Employee = Person()
print(Employee.get_Name())
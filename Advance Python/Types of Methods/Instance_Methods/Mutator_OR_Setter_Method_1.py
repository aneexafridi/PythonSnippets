# --------------- Mutator Method
# This method is used to access or read and modify data of the variables.
# This method modify the data in the variable.
# This is also called as setter method.

# Ex:---
# 	def set_Name(self):
# 	def set_Roll(self):

class Person:
	def __init__(self): # constactor or special method
		self.Name = "Equal" # Instance variable
	def set_Name(self,name): # Mutator or setter Method
		self.Name = name

employee = Person()
employee.set_Name("Test")
print(employee.Name)
print(Person().Name)
# -----Accesssing Instance Variable
#---------------
# Outsite Class
#---------------
# we can access instance variable using
# object_Name.variable_Name
# Example:
# 		class Person:
# 			def __init__(self):
# 				self.Name = "Equal"
# 			def Person_Name(self):
# 				print(self.Name)
# 		p = Person()
# -------------------------------------------------------------
class Person:
	def __init__(self):
		self.Name = "Equal" # instance variable
	def Person_Name(self): # instance Method
		print(self.Name)  # accessing instance variable
Person().Person_Name()
print(Person().Name)  # accessing outside the class




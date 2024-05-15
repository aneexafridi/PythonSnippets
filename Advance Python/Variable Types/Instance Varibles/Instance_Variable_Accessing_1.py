# -----Accesssing Instance Variable
#----------------------
# With Instance Method
#----------------------
# To access instance variable, we need instance Method
# with self as first parameter then we can access instance
# variable using self.variable_Name
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





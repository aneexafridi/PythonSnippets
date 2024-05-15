# ------------Accessing Class/Static Variable
# ---------------
# with in Class Method
# ---------------------
# To access class/Static Variable, we need class methods
# with cls as first parameter then we can access class
# Variable using cls.Variable_Name.
# Example:--
# 		class Person:
# 			Age  = 10 # Class / Static Variable
# 			def __init__(self):
# 				sell.Name = "Equal" # Instance variable
# 			def Person_Name(self):
# 				print(self.Name)
#			@classmethod
#			def Person_Age(cls): # first must cls parameter
#               print(cls.Age)
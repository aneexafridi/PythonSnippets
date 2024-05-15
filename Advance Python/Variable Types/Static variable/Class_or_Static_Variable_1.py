# -----Class variable/ Static variable
# Class variable are the variable whose single copy is avaible to
# all the instance/object of the class.
# If we modify the copy of class variable in an instance, it will
# effect all the copies in the other instance.
# Example:--
# 		class Person:
# 			Age  = 10 # Class / Static Variable
# 			def __init__(self):
# 				sell.Name = "Equal" # Instance variable
# 			def Person_Name(self):
# 				print(self.Name,Age)

# class.class_variable_Name # to access outside from the class
# Person.Age
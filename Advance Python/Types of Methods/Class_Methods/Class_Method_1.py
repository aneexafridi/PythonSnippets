# -----------------Class Methods
# class methods are the methods which act upon the
# class variables or static variable of the class.

# Decorator @classmethod need to write above the class method.
# By default, the first parameter of class method is cls
# which refers to the class itself.

# Syntax:----
# 			@classmethod --> Decorator
# 			def method_Name(cls):  class method no parameter
# 				method body
# 			@classmethod
# 			def method_name(cls,p1,p2): class method with parameter
# 				method body

class Person:
	@classmethod
	def Person_Name(cls):
		print("Eqaul")
	@classmethod
	def Person_Roll(cls,Roll):
		print(Roll)
# To call the class method  use The Class Name
Person.Person_Name()
Person.Person_Roll(38)

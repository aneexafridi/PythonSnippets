# ------------Static Methods
# Static mehods are used when some processing is related to
# the class but does not need eh class or its instances to
# any work.
# We use static method when we want to pass some values from
# outside and perform some action in the method.
# Decorator @staticmethod need to write above the static method.

class Person:
	Id = 11 # class variable
	@staticmethod # decorater
	def Person_Name(): # static method with no parametor
		print("Equal") 
	@staticmethod # decorator
	def Person_Roll(roll): # static method with parametor
		print(roll)
	@classmethod # decoratro
	def Person_Id(cls): # class method with parameter
		print(cls.Id)
		
Person.Person_Name()
Person.Person_Roll(38)
Person.Person_Id()
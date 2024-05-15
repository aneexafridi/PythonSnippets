# A static method does not receive an implicit first argument.
# To declare a static method

class Student(object):
	@staticmethod
	def Name(): # static method does not pass first argument
		print("static Method")


Student.Name()
S = Student()
S.Name()
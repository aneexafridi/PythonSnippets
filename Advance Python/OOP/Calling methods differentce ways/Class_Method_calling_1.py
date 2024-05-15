# A class method receives the class as implicit first argument,
# just like an instance method receives the instance.

class Student(object):
	@classmethod
	def Name(cls): # must pass the first argument
		print("class Method")


Student.Name()
S = Student()
S.Name()
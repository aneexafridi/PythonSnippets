class Student(object):
	def Name(self): # must be write first argument of instance method
		print('Instance Method')



Student().Name()   # Not working "Student.Name()"
# beacuse this is the instance method not a class or static method
S = Student()
S.Name()
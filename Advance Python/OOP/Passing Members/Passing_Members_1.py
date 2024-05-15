# Passing Members of one Class to Another Class
class Student:
	# constructor/special method
	def __init__(self,Name,Roll):
		self.Name = Name
		self.Roll = Roll

	# Instance Method
	def Student_Data(self):
		print("Student Name: ",self.Name)
		print("Student Roll: ",self.Roll)

class User:
	@staticmethod # decorater
	def Show(data): # method with parameter
		data.Student_Data() # here calling the Student class method 

student_1 = Student("Equal",38)
# passing as object to static method "Show" of User Class
User.Show(student_1) 

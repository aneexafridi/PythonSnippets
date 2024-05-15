# -------------Nested Class
# A class hava inner another class is called Nested Class

class University:
	def __init__(self,Uni_Name,Stud_Name,Roll):
		self.Uni_Name = Uni_Name
		self.New_Studend = self.Student(Stud_Name,Roll)
	def University_Name(self):
		print("University Name: ",self.Uni_Name)



	class Student:
		def __init__(self,student_Name,Roll):
			self.student_Name = student_Name
			self.Roll = Roll
		def Studend_Data(self):
			print("Student Name: ",self.student_Name)
			print("Student Roll: ",self.Roll)



Test = University("Kust","Equal",38)
Test.University_Name()
Test.New_Studend.Studend_Data()
# we can write the Test.New_Student like this
# S1 = Test.New_Studen
# S1.Student_Datat() == Test.New_Student.Student_Data()


# Note -----------
# We Can Create the object/instance of Inner Class  from  outer class
# Test = University().Student()  




from abc import ABC,abstractmethod

class Person(ABC):
	def __init__(self,Name,Roll):
		self.Name = Name
		self.Roll = Roll
	@abstractmethod
	def Age(self):
		pass
class Student(Person):
	def Age(self):
		print("None of my bisness")
		print(f'Name : {self.Name} and Roll {self.Roll}')

S = Student("Shahab",55)
S.Age()
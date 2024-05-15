# 					@abc.abstractmethod
# A decorator indicating abstract methods.

# Using this decorator requires that the class’s metaclass is ABCMeta or
 # is derived from it. A class that has a metaclass derived from ABCMeta
 # cannot be instantiated unless all of its abstract methods and properties 
 # are overridden. The abstract methods can be called using any of the normal 

# abc is module and ABC is class(abstract built-in)
# abstractmethod is function which in abc module
from abc import ABC,abstractmethod

class Person(ABC):
	@abstractmethod
	def Name(self,Name):
		pass

class Student(Person):
	def Name(self,Name=None): # by default set Name = None
		print(f'Yours name is "{Name}"')

S = Student()
S.Name("Name")
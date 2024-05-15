# -----------------------Constructor in Inheritance
# By default, The Constructor in the parent class is available 
# to the child class.
# Example:--
class Vehicle(object):
	def __init__(self):
		self.Name = "Lambergani"
		print("Constructor of Super Class")
	def Vehicle_Type(self):
		print("Super Class of Vehicle:")

class Car(Vehicle):
	def Show_data(self):
		print("Vehicle Name: ",self.Name)
		print("Sub Class of Vehicle")

car = Car()
car.Vehicle_Type() # call the super class instance method
car.Show_data() # call the sub class instance method use attributes
# of super class which is self.Name of Vehicle class
#--------------------Single Inheritance
# If a class is derived from one base (Parent Class), it is
# called Single Inheritance.
# Syntax:--
# 	class Parent_Class_Name(object):
	# 		Memeber of Parent Class
	# class Child_Class_Name(Parent_Class_Name):
	# 	Memeber of Child Class


class Vehicle(object):
	vehicle_no = "ICT38"
	@classmethod
	def Show_Vehicle_No(cls):
		print("Super Class\nVehicle Number: ",cls.vehicle_no)
	def Vehicle_Name(self):
		print("Super Class\nVehicle Name is Alambergani")
	@staticmethod
	def Vehicle_Pirce():
		price = 4_0000_00
		print("Super Class\nVechile Price: ",price)

class Car(Vehicle):
	def Show_Car(self):
		print("Alto Car!!! Child Class")

car  = Car()
car.Show_Car()
car.Show_Vehicle_No()
car.Vehicle_Name()
car.Vehicle_Pirce()

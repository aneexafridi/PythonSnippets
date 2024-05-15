from abc import ABC,abstractmethod

class Defance_Fore(ABC):
	def __init__(self):
		print("Abstract Class Constractor")
	@abstractmethod
	def Area(self):
		pass
	def Gun(self):
		print("Gun is : AK47")

class Army(Defance_Fore):
	def Area(self):
		print("Abstract Method")
		print("Area of Army Sky")

class Airforce(Defance_Fore):
	def Area(self):
		print("Abstract Method")
		print("Area of Airforce: Sky")

class Navy(Defance_Fore):
	def Area(self):
		print("Abstract Method")
		print("Area of Navy: Sea")

army = Army()
army.Area()
army.Gun()
print()
airforce = Airforce()
airforce.Area()
airforce.Gun()
print()
navy = Navy()
navy.Area()
navy.Gun()

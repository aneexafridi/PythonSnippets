from abc import ABC,abstractmethod

class Defence(ABC):
	@abstractmethod
	def Gun(self):
		pass
	@abstractmethod
	def Area(self):
		pass
# class Army(Defence):
# 	def Gun(self):
# 		print("Army Gun = AK47")
# 	def Area(self):
# 		print("Army Area = Land")
# class AirForce(Defence):
# 	def Gun(self):
# 		print("AirForce Gun = G3")
# 	def Area(self):
# 		print("AirForce Area = Sky")
# class Navy(Defence):
# 	def Gun(self):
# 		print("Navy Gun = J99")
# 	def Area(self):
# 		print("Navy Area = Sea")
# army = Army()
# army.Gun()
# army.Area()
# print()
# airforce = AirForce()
# airforce.Gun()
# airforce.Area()
# print()
# navy = Navy()
# navy.Gun()
# navy.Area()


# help(Defence)
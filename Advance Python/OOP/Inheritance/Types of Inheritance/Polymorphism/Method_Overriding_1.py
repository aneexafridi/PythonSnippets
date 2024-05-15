# ---------------Method Overriding
# If we write method in the both classes,parent Class and Child Class then
# the parent Class's method is not available to the child Class.
# In this case child Class's method is accessible which means child Classs's
# Method is replacing parent Class's method.
# Method Overriding is used when programmer want to modify the existiong behavior
# of a Method. 

# --------------------super() Method
# this method is used to call parent Class's constructor or Methods form
# the child Class.
# When Same name method and Constructor will use super() method

class Vehicle:
	def Start(self):
		print("Vehicle Already!!)")
class Car(Vehicle):
	def Start(self):
		print("Car Already))")
		super().Start()
car = Car()
car.Start()


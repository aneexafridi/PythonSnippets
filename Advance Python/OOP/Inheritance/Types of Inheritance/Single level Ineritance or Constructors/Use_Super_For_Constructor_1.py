# -----------------Constructor with super() Method
# If we write constructor in the both classes, parent class and child class
# then the parent class constructor is not available to the child class.
# In this case only child class constructor is accessible which means
# child class constructor is replacing the parent class constructor.

# super() Method is used to call parent class constructor or Methods
# from the child class.
class Father:
	def __init__(self):
		self.Father_Money = 2_00_00 # instance variable
		print("Father Money: ",self.Father_Money)

class Son(Father):
	def __init__(self):
		super().__init__() # calling parent class constructor
		self.Son_Money = 1_00_00 # instance variable
		print("Son Money : ",self.Son_Money)
	def Son_property(self):
		super().__init__()

s = Son()
s.Son_property()
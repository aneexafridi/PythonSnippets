# -----------------------Constructor in Inheritance
# if we write constructor in the both classes, parent class and child class
# then the parent class constructor is not available to the child class.
# In this case only class constructor is accessible which means child class 
# constructor is replacing parent classs constructor.

# Constructor ovrriding is used when programmer want to modify the existiong
# behavior of a constructor.
class Father:
	def __init__(self):
		self.Father_Money = 2_00_00 # instance variable
		print("parent Money: ",self.Father_Money)
class Son(Father):
	def __init__(self):
		self.Son_Money = 1_00_00 # instance variable
		print("Son Money is : ",self.Son_Money)
s = Son()


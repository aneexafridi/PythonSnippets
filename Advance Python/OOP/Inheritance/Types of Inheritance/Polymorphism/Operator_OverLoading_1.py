# -----------------Operator Overloading
# If any operator performs additional actions other than what it is mean
# for, it is called operator Overloading.

# print(10+20)
# print(int.__add__(10,20))
# # integer Class have int.__add__(self,other)

# print("Equal "+"equal")
# print(str.__add__("Equal ","equal"))

# adding two objects which is overloading
class A:
	def __init__(self,Object):
		self.Object= Object
	def __add__(self,Object):
		return self.Object+Object.Object
class B:
	def __init__(self,Object):
		self.Object=Object

a = A(100)
b = B(200)
print(a+b) # behind process A.__add__(a,b)


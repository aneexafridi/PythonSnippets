# -------------------Multiple Inheritance
# If a Class is derived from one than more Super Classes,
# then It is called Multiple Inheritance

class Father(object):
	def Father_Property(self):
		print("Father Class Property")
class Mother(object):
	def Mother_Property(self):
		print("Mother Class Property")

class Son(Father,Mother):
	def Son_Property(self):
		print("Son Class Property")

son = Son()
son.Son_Property()
son.Father_Property()
son.Mother_Property()
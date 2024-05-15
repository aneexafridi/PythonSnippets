# Father class two or more  than inheritance its called hierarchical inheritance
# Father class can be inhertance more sub Classes.

class Father(object):
	def Father_property(self):
		print("Father Property:))")
class Son(Father):
	def Son_property(self):
		print("Son Property")
class Daughter(Father):
	def Daughter_property(self):
		print("Daughter Property")
son = Son()
son.Son_property()
son.Father_property() # calling Father class instance method
print()
daugther = Daughter()
daugther.Daughter_property()
daugther.Father_property() # calling Father class instance method
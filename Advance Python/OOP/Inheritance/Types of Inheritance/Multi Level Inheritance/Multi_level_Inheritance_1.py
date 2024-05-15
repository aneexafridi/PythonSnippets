# ----------------------Multi-level Inheritance
# In multi-level Inheritance, the Class Inherits the feature of another derived
# class (Child Class).
# Syntax:
# class Father(object):
# 	members of Father Class
# class Son(Father):
# 	members of Son Class
# class Grand_Son(Son):
# 	members of Grand_Son Class
class Father(object):
	def Father_property(self):
		print("*"*20,"\nFather Class Method")
class Son(Father):
	def Son_property(self):
		print("*"*20,"\nSon Class Method")
class Grand_Son(Son):
	def Grand_Son_Property(self):
		print("*"*20,"\nGrand son Class Method")

G_son  = Grand_Son()
G_son.Grand_Son_Property()
G_son.Son_property()
G_son.Father_property()
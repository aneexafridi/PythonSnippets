# ------------------Method Overloading
# When more than one method with the same name is defined
# in the same Class,
# it is know as method overloading.
# In python, If a method is written such that it can perform more
# than one task,it is called method overloading.
# we achieve method overloading by writing same method with several
# parameters.
class Load:
	def Sum(self,x=None,y=None,z=None):
		if x==None and y==None and z == None:
			return None
		elif x!=None and y==None and z == None:
			return x
		elif x==None and y!=None and z == None:
			return y
		elif x==None and y==None and z != None:
			return z
		elif x!=None and y!=None and z!=None:
			return x+y+z
		elif x!=None and y!=None and z==None:
			return x+y
		elif x!=None and y==None and z!=None:
			return x+z
		elif x==None and y!=None and z!=None:
			return y+z

load = Load()
print(load.Sum(3,4,4))
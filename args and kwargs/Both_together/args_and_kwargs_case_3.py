# case 3
class A(object):
	def __init__(self,b,c):
		self.b=b
		self.c=c
class B(A):
	def __init__(self,a,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.a = a
b = B(1,2,3)

print(b.a)
print(b.b)
print(b.c)

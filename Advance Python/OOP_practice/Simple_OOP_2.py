class Show(object):
	def __init__(self,Name):
		self.Name = Name
	def Show_data(self,price):
		self.price = price
		print("Mobile Name: ",self.Name,"price: ",self.price)
A = Show("Samsang")
A.Show_data(88888)
B = A.copy()
B.Show_data(99999)
print(id(A))
print(id(B))

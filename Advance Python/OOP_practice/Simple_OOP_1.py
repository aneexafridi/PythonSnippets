# object  is the super class name which is inherient
# self is variable which is refer to current class object/instance

class Show(object):
	def Show_data(self):
		print("Equal!=equal")
A = Show()
B = Show()
A.Show_data()
B.Show_data()
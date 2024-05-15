

class Father(object):
	def __init__(self):
		print("Father Class Constructor")
class Son(Father):
	def __init__(self):
		print("Son Class Constructor")
		super().__init__()
class Grand_Son(Son):
	def __init__(self):
		print("Grand son Class Constructor")
		super().__init__()

G_son  = Grand_Son()
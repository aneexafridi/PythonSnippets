class Father(object):
	def __init__(self):
		print("Father Class Constructor")
# Object class constructor calling here
		super().__init__() 

class Mother(object):
	def __init__(self):
		print("Mother Class Constructor")
# Object class constructor calling here
		super().__init__()

class Son(Father,Mother):
	def __init__(self):
		print("Son Class Constructor")
# Parents class constructor calling here
		super().__init__()
		
son = Son()

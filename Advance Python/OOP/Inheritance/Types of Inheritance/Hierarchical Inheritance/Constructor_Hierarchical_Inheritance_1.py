# Father class two or more  than inheritance it called hierarchical inheritance
# Father class can be inhertance more sub Classes.
class Father(object):
	def __init__(self):
		print("Father Class Constructor:))\n")
class Son(Father):
	def __init__(self):
		print("Son Class Constructor")
		super().__init__() # call the Father class Constructor
class Daughter(Father):
	def __init__(self):
		print("Daughter Class Constructor")
		super().__init__() # call the Father class Constructor


son = Son()
daughter = Daughter()
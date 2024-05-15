# ---------------Constructor
# python supports a special type of method
# called Constructor for initiallizing the
# instance variable of a class.
# A class Constructor, if defined is called
# whenever a program creates an object of
# that class.
# A constracator is called only onnce at the
# time of creating an instance.
# If two instances are created for a class,
# the constracator will be called onnce for
# each instance.

class Person(object):
	def __init__(self):
		print("Without parameter Constructor")

# P1 = Person()
Person()
# i do not need to create a object/instance
# of person class because there is no
# attributes for using for objects
# that's why



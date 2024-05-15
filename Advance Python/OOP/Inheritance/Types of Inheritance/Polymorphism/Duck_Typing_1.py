# -------------------------Duck Typing
# In Python, we follow a priciple - If it walks like a duck and talks like a duck,
# it must be a duck, Which means python doesn't care about which class of object it
# is,if it is an object and required behavior is present for that object
# then it will work. The type of object is distinguished only at runtime.
# This is called as duck typing.

# Python doesn't care about which class of object it is,in order to call an
# existing method on an object. If the method is defined on the object,then it
# will be called

class Dog(object):
	def Sound(self):
		print("Dog Sound\nwoop woop woop")
class Cat(object):
	def Sound(self):
		print("Cat Sound\nmio mio mio")

def Checking(Pass_Object):
		Pass_Object.Sound()

dog = Dog()
cat = Cat()

Checking(dog)
Checking(cat)

# help(hasattr)
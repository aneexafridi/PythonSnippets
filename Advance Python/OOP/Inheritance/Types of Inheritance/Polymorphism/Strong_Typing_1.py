# ------------------------strong Typing
# we can check whether the object passed to the method has the
# method being invoked or not.
# hasattr() Function is used to check whether the object has a method
# or not.
# Syntax:====
# 			hasattr(object,attribute)
# 		Where attribute can be a method or variable. if it is found in
# 		the object then this method returns True else False.


class Dog(object):
	def Sound(self):
		print("Dog Sound\nwoop woop woop")
class Cat(object):
	def Sound(self):
		print("Cat Sound\nmio mio mio")
class Person(object):
	def Talk(self):
		print("Person Talk\nyes yes yes")

def Checking(Pass_Object):
	if hasattr(Pass_Object, 'Sound'):
		Pass_Object.Sound()
	elif hasattr(Pass_Object, 'Talk'):		
		Pass_Object.Talk()

dog = Dog()
cat = Cat()
person = Person()

Checking(dog)
Checking(cat)
Checking(person)

# help(hasattr)
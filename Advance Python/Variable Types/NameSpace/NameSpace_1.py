# ------------------NameSpace
# In Python, Namespace represents a memory block
# where names are mapped to objects

# Class Namespace -- A class maintains it's own namespace known as class
# namespace.In the class namespace, then names are mapped to
# class variables.

# Instance Namespace -- Every Instance have it's own namespace known as
# Instance namespace. In the Instance namespace, the names are mapped
# to Instance variables.

class Person:
	Age = 99 # Class/ static variable
# Age value == class Namespce

Ali = Person()
Fawad = Person()
print("Ali and Fawad  value instance Namespace")
print(Person.Age)
print(Ali.Age)
print(Fawad.Age)
print()
print("after change the value of Class/static  variable  with Class")
Person.Age = 100
print(Person.Age)
print(Ali.Age)
print(Fawad.Age)
print()

print("after change the value of Class/static  variable with Object")
Ali.Age = 105
print(Person.Age)
print(Ali.Age)
print(Fawad.Age)


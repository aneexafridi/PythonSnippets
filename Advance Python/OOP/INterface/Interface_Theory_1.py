# ----------------------------Interface----------------------------------
# In Python, The interface concept is not explicitly, Like available in
# other languages e.g java
# In Python, an interface is an abstract Class which contains only abstract
# method but not a single concrete method.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# --------------------How to make Interface----------------------------
# from abc import ABC, abstractmethod
# 		class Class_name(ABC):
# 		@abstractmethod
# 		def Show(self):
# 			pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ------------------------------Roles--------------------------------------
# All methods of an interface is abstract.
# We can not create object of interface.
# If a Class is implementing an interface it has to define all the methods
# given in that interface.
# If a Class does not implement all the methods declared in the Interface,
# the Class must be declared abstract.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ________________________When use Interface_______________________________
# We use interface When all the features need to be implemented differently
# for different objects.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#___________________________Abstract Class VS Interface__________________________
# >> An abstract Class Can have abstract methods as Well as Create mehtods,But
#    all methods of an interface are abstract.
# >> We use abstract Class When there are some common Feature Shared by all
#    the objects as they are while we use interface if All the feature need to
#    be implemented differently for different objects.
# >> Its programmer job to write child Class for abstract Class While in
# interface, any third party vendor will take responsibility to write child Class.
# >> Interfaces are slow when compared to abstract Class.
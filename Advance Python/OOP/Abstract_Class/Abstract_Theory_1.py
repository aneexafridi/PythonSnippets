# ------------------Abstract Class
# A Class derived from ABC Class whic belongs to abc module,is known as Abstract
# Class in Python.

# ABC Class is known as Meta Class which means a Class that defines the behavior
# of other Classes.So we can say,Meta Class ABC defines that the Class which is
# Derived from it becomes an Abstract Class.

# Abstract Class can have Abstract Method and concrete methods.
# Abstract Class needs to be extended and its methods implemented.
# PVM (python virtual machine)can can create objects of an abstract Class.
# Exameple:--
# 		from abc import ABC,abstractmethod
# 		class Class_Name(ABC):
# -------------------------------------------------------------------------------
# -----------------------Abstract Method
# A Abstract method is a method whose action is refined in the child Classes as
# per the requirement of the object.
# We can declare a method as abstract method by using @abstractimethod decorator.
# Exameple:--
# 		from abc import ABC,abstractmethod
# 		class class_Name(ABC):
# 			@abstractmethod
# 			def Display(self):
# 				pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -----------------------Concrete Method
# A concrete method is a method whose is defined in the Abstract Class itself.
# Example:--
# 		from abc import ABC,abstractmethod
# 		class Class_Name(ABC):
# 			@abstractmethod
# 			def Display(self):
# 				pass
# 			def view(self): # Conrete method
# 				print("Conrete method")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# _______________________________Rules____________________________________________
# >> PVM can not create objects of an abstract Class.
# >> It is not neccessary to declare all methods abstract in a abstract Class.
# >> Abstract Class can have Abstract method and concrete methods.
# >> If there is any Abstract method in a Class, that Class must be abstract.
# >> The Abstract methods of an Abstract Class must be defined in its child Class/subClass.
# >> If you are inheriting any abstract Class that have abstract Class that have abstract
#    method, you must either provide the implementation of the method or make this Class
#    Abstract.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -------------when use Abstract Class
# we use abstract Class when there are some common feature shared by all the objects as They are.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#___________________________Abstract Class VS Interface__________________________
# >> An abstract Class Can have abstract methods as Well as Create mehtods,But
#    all methods of an interface are abstract.
# >> We use abstract Class When there are some common Feature Shared by all
#    the objects as they are while we use interface if All the feature need to
#    be implemented differently for different objects.
# >> Its programmer job to write child Class for abstract Class While in
# interface, any third party vendor will take responsibility to write child Class.
# >> Interfaces are slow when compared to abstract Class.
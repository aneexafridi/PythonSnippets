# ===================Set and Get Thread Name===================
# >> current_thread() - This function return current thread Object.
# >> getName() - Every thread has anme by delault, to get the name
# of thread we can use this method.
# >> setName(give_name)- This method is used to set the name of the thread.
# >> name Property - This property is used to get or set name of the thread.



# also import the from the threading mudule
# the Thread class and current_thread function
from threading import Thread,current_thread
def Child():
	print("Default Child Thread Object: ",current_thread().getName())
	current_thread().setName("Child Thread")
	print()
	print("New Child Thread Object: ",current_thread().getName())

Child_object = Thread(target=Child)
Child_object.start()
print()
print("Default Main Thread Object: ",current_thread().getName())
current_thread().setName("Main Thread:)")
print()
print("New Main Thread Object: ",current_thread().getName())

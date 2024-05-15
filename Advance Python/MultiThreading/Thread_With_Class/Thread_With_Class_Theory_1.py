# =================Creating Thread===============
# Thread Class of threading module is used to creat threads. to create own
# thread we need to create an Object of Thread Class.
# Following are the ways of creating threads:---
# >>Creating a thread by creating a Child Class to built-in Thread Class.
# ________________________________________________________________________
# Creating a thread by creating a child Class to Thread Class
# We can create our own thread Child Class by inheriting Thread Class built-in form threading module.
# Syntax:
# 		class Child_thread_name(Thread):
# 			statements

# 		child_object = Child_thread_name()
from threading import Thread

class Child_thread(Thread):
	pass
child_object = Child_thread()
print(child_object.getName())
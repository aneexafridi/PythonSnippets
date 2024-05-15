# -----------Thread Synchronization--------------
# Many threads trying to access the same object can lead to problems
# like making data inconsistent or getting unexpected output so when a
# Thread is alread accessing an object,Preventing any other Thread 
# accessing the same object is called Thread Synchronization.
# The object on which the threads are synchronized is called
# Synchronized Object or Mutually Exclusive Lock(mutex)
# Thread Synchronization is recommended when multiple threads
# are acting on the same object simultaneously.
# There are following techniques to do Thread Synchronization:
#  Using Locks
#  Using RLock(Re-Entrant Lock)
#  Using Semaphores.
# -------------------------------------------------------------------------
# -===========================Locks=============================
# Locks are typically used to synchronize access to a shared resource. Lock can
# be used to lock the object in which the thread is acting. A lock has only two
# states, locked and unlocked. It is created in the unlocked state.
# =============================================================================
# --------------------------------acquire()
# This method is used to changes the state to locked and returns immediately.
# When the state is locked, acqure() blocks until a call to release() in another
# Thread changes it to unlocked, then the
# Syntax: -- 
# 		acquire(blocking = True ,timeout= -1)
# 	>> True - It blocks until the lock is unlocked, then set it to locked and
# 	return True.
# 	>> False - It does not block.If a call with blocking set to True would block,
# 	return False immediately,otherwise,set the lock to locked and return true.
# 	>> Timeout -- When invoked with the floating-point timeout argument set to 
# 	a positive value,Block for at most the number of seconds specified  by timeout
# 	long as the lock cannot be acquired. A timeout argument of -1 specifies an
# 	unbounded wait. It is forbidden to specify a timeout whin blocking is false.
# 	============================================================================
# 	-----------------------------release()-----------------------------
# 	This method is used to release a lock.This can be called from any thread,
# 	not  only the thread which has acquired the lock.
# 	When the lock is locked, reset it to unlocked, and return. If any other threads
# 	are blocked waitin gro the lock to become unlocked, allow exactly one of 
# 	them tho procced.
# 	When invoked on an unlocked lock, a RuntimeError is raised.
# 	There is no return value.
# 	Syntax: -- release()
# -------------------------------------------------------------------------------------

from threading import *
class Ticket:
	def __init__(self,available_Tickets):
		self.available_Tickets = available_Tickets
		self.Lock_object = Lock() # create lock class object/instance
	def Book_Ticket(self,book_ticket):
		self.Lock_object.acquire(blocking=True,timeout=1) # method of Lock() Class
		print("Available Tickets: ",self.available_Tickets)
		if(book_ticket<=self.available_Tickets):
			name = current_thread().getName()
			print("Client Name: ",name)
			print(f'{book_ticket} ticket booked for {name}')
			self.available_Tickets -=book_ticket
		else:
			print("Sorry: we have not availables Tickets Right Now:)")
		self.Lock_object.release() # release
ticket = Ticket(2)
Fawad = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Fawad')
Zeeshan = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Zeeshan')
Shahab = Thread(target=ticket.Book_Ticket,args=(1,),name="Shahab")
Fawad.start()
Zeeshan.start()
Shahab.start()

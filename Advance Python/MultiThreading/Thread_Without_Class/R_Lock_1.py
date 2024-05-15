# ---------------------RLock
# A reentrant lock is a synchronization primitive that may be acquired
# multiple times by the same thread.
# The standard Lock doesn't know which thread is currently holding the lock.
# If the lock is held, any thread that attempts to acquire it will block,even if the
# same thread itself is already holding the lock.
# In such cases,RLock(re-entrant lock) is used.

# A reentrant lock must be released by the thread that acquire it.
# Once a thread has acquired a reentrant lock, The same
# Thread may acquire it again without blocking; the thread must released
# it once for each time it has acquired it.

from threading import *
class Ticket:
	def __init__(self,available_Tickets):
		self.available_Tickets = available_Tickets
		self.RLock_object = RLock() # create RLock class object/instance
	def Book_Ticket(self,book_ticket):
		# method of Lock() Class
		self.RLock_object.acquire() 
		self.RLock_object.acquire()
		self.RLock_object.acquire()

		print("Available Tickets: ",self.available_Tickets)
		if(book_ticket<=self.available_Tickets):
			name = current_thread().getName()
			print("Client Name: ",name)
			print(f'{book_ticket} ticket booked for {name}')
			self.available_Tickets -=book_ticket
		else:
			print("Sorry: we have not availables Tickets Right Now:)")
		self.RLock_object.release() # release
		self.RLock_object.release()
		self.RLock_object.release()
ticket = Ticket(2)
Fawad = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Fawad')
Shahab = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Shahab')
Zeeshan = Thread(target=ticket.Book_Ticket,args=(1,),name="Zeeshan")
Fawad.start()
Shahab.start()
Zeeshan.start()

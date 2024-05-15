# ----------------------Semaphore---------------
# this is one of the oldest synchronization primitives in the history
# of computer science,invented by the early Dutch computer seientist Edsger W.Dijkstra,
# from threading import*
# help(Semaphore.acquire)
from threading import *
class Ticket:
	def __init__(self,available_Tickets):
		self.available_Tickets = available_Tickets
		self.Semaphore_object = Semaphore(2) # create lock class object/instance
	def Book_Ticket(self,book_ticket):
		self.Semaphore_object.acquire(blocking=True,timeout=1) # method of Thread() Class
		print("Value: ",self.Semaphore_object._value)
		print("Available Tickets: ",self.available_Tickets)
		if(book_ticket<=self.available_Tickets):
			name = current_thread().getName()
			print("Client Name: ",name)
			print(f'{book_ticket} ticket booked for {name}')
			self.available_Tickets -=book_ticket
		else:
			print("Sorry: we have not availables Tickets Right Now:)")
		self.Semaphore_object.release() # release
ticket = Ticket(2)
Fawad = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Fawad')
Zeeshan = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Zeeshan')
Shahab = Thread(target=ticket.Book_Ticket,args=(1,),name="Shahab")
Fawad.start()
Zeeshan.start()
Shahab.start()


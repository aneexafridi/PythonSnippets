from threading import Thread,current_thread
class Ticket:
	def __init__(self,available_Tickets):
		self.available_Tickets = available_Tickets
	def Book_Ticket(self,book_ticket):
		print("Available Tickets: ",self.available_Tickets)
		if(book_ticket<=self.available_Tickets):
			name = current_thread().getName()
			print("Client Name: ",name)
			print(f'{book_ticket} ticket booked for {name}')
			self.available_Tickets -=book_ticket
		else:
			print("Sorry: we have not availables Tickets Right Now:)")

ticket = Ticket(1)
Fawad = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Fawad')
Zeeshan = Thread(target=ticket.Book_Ticket, args=(1,) ,name='Zeeshan')
Fawad.start()
Zeeshan.start()
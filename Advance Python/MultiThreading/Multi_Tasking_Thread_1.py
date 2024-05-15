# -----Multitasking using Multiple Thread
# When multiple tasks are executed at a time, then it is called Multi-tasking.
# For this purpose we need more than one thread and when we use more than one
# Thread.it is Called multi threading.

# Two Task using Two Thread
from threading import Thread

class Restaurant:
	def __init__(self,a):
		self.a = a

	def Food(self):
		for u in range(1,6):
			print(self.a,u)
		print()

R1 = Restaurant("Take order from Table ")
R2 = Restaurant("Serve Order to Table ")
Thread_1 = Thread(target=R1.Food)
Thread_2 = Thread(target=R2.Food)
Thread_1.start()
Thread_2.start()
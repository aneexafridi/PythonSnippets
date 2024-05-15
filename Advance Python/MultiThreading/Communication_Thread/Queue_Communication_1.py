# ----------------Queue class in threading module
from threading import Thread
from queue import Queue
from time import sleep

class Producer:
	def __init__(self):
		self.queue = Queue() # create object

	def produce(self):
		for u in range(1,6):
			print("Item produced",u)
			self.queue.put(u)
			sleep(1)
class Consumer:
	def __init__(self,prod):
		self.prod = prod
	def consume(self):
		for u in range(1,6):
			print("Item Received",self.prod.queue.get(u))
		print("done.....")
producer = Producer()
consumer = Consumer(producer)

thread_1= Thread(target=producer.produce)
thread_2 = Thread(target=consumer.consume)
thread_1.start()
thread_2.start()




# =============run() Method
# run() - Every thread will run this method when thread is started.
# we can override this method and write our own code as body of the
# method.
# A thread will terminate automatically when it comes out of then
# run() Method.

# for more information of the  run method
# help(Thread.join)
from threading import Thread
class MyThread(Thread):
	def run(self): # override the run method
		for u in range(3):
			print("child Thread")
My_thread_object = MyThread()
My_thread_object.start()

for v in range(3):
	print("Main Thread")
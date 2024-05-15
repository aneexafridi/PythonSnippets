# ================join() Method
# This method is used to wait till the thread completely
# executes the run() Method.



from threading import Thread
# for more information about the join Method
# help(Thread.join)

class MyThread(Thread):
	def run(self): # override the run method
		for u in range(3):
			print("child Thread")

My_thread_object = MyThread()
My_thread_object.start()
print(My_thread_object.is_alive())
My_thread_object.join()
for v in range(3):
	print("Main Thread")
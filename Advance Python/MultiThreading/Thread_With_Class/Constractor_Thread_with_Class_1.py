# ==========Constructor=====================
# from threading import Thread
# class MyThread(Thread):
# 	def __init__(self,a):
# 		Thread.__init__()
# 		self.a = a
# My_object = MyThread(100)

from threading import Thread
class MyThread(Thread):
	def __init__(self):
		print("Child Thread Constructor")
		Thread.__init__(self)

My_object = MyThread()
My_object.start()
print("Main Thread")
from threading import Thread
from time import sleep
class MyTest:
	def Solve_Question(self):
		self.q_1()
		sleep(2)
		self.q_2()
		sleep(2)
		self.q_3()
		sleep(1)
		print("Done")
	def q_1(self):
		print("Question 1 solved")
	def q_2(self):
		print("Question 2 solved")
	def q_3(self):
		print("Question 3 solved")

Test = MyTest()
MyThread = Thread(target=Test.Solve_Question)
MyThread.start()

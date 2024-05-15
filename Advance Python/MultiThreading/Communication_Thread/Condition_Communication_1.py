from threading import Thread, Condition
from time import sleep
# help(Condition)
List = list()
def Produce():
	condition_object.acquire()
	for u in range(1,10):
		List.append(u)
		sleep(1)
		print("Item Produceed---")
	condition_object.notify()
	condition_object.release()
def Consume():
	condition_object.acquire()
	condition_object.wait(timeout=0)
	condition_object.release()
	print(List)

condition_object = Condition()
thread_1 = Thread(target=Produce)
thread_2 = Thread(target=Consume)
thread_1.start()
thread_2.start()
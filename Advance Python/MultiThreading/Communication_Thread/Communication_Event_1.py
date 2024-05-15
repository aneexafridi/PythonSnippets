# ----------------------Event Class in threading module
# from module_name import * astrek mean include all in this module
from threading import Thread,Event
from time import sleep # sleep method from time
# help(Event)
# traffic lights

def light_swith():
	print('.....')
	sleep(3)
	event.set() # set method set the flag True
	print("Gree light ON")
	sleep(5)
	print("Red light ON")
	event.clear() # set method set the flag False
def Traffic():
	event.wait()
	while event.is_set():
		print("Now u can Go.....")
		sleep(0.5)
	print("Stop")
	print("Program Done...")

event = Event()

thread_1 = Thread(target=light_swith)
thread_2 = Thread(target=Traffic)
thread_1.start()
thread_2.start()
from threading import Thread,current_thread
from time import sleep,perf_counter

def Do_something():
	for u in range(1,11):
		print(u,end=' ')
	print()

T1 = Thread(target=Do_something)
T2 = Thread(target=Do_something)

T1.start()
T2.start()

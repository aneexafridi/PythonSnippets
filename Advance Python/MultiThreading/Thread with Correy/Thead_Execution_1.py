from threading import Thread,current_thread
from time import sleep,perf_counter

Start = perf_counter() # return float value

def Do_something():
	print("Sleeping for one 1 Seconds")
	sleep(1)
	print("\nDone Sleep....")

thread_1 = Thread(target=Do_something)

thread_1.start()

thread_1.join()


Finish = perf_counter()


print(f'\nFinish code {round(Finish-Start,2)} Seconds')


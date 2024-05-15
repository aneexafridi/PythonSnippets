from threading import Thread,current_thread
from time import sleep,perf_counter

Start = perf_counter() # return float value

def Do_something():
	print("Sleeping for one 1 Seconds")
	sleep(1)
	print("Done Sleep....")

Join_list = list()

for _ in range(10): # here _ mean nothing with numbers
	Thread_obj=Thread(target=Do_something)
	Thread_obj.start()
	Join_list.append(Thread_obj)

# now we neet to join method use to 
# execute the after one by one

for J in Join_list:
	J.join()


Finish = perf_counter()

print(f'\nFinish code in {round(Finish-Start,2)} Second(s)')


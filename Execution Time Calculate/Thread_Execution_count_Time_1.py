from threading import Thread,current_thread
from time import sleep,perf_counter,ctime

Start_t = perf_counter()

def Run():
	print('Sleep for 1 Seconds....')
	sleep(1)
	print("done the program")

T_1 = Thread(target=Run)
T_2 = Thread(target=Run)
T_1.start()
T_2.start()
T_1.join() # join method wait for till to finish the thread
T_2.join()
L = []

for _ in range(10):
	t=Thread(target=Run)
	t.start()
	L.append(t)
for s in L:
	s.join()



End_t = perf_counter()
print()
print(f'Finish with {round(End_t-Start_t,2)} Seconds')










s = 'abc'
print(s[-2:])








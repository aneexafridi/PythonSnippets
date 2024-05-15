# When non-Daemon Thread terminate then also teriminate Daemon Thread
from threading import Thread ,current_thread
from time import sleep
def Teacher():
	for u in range(1,11):
		print("Teaching Session:",u)
		sleep(1)

thread_1 = Thread(target=Teacher)
thread_1.setDaemon(True)
thread_1.start()
sleep(5)
print("Exam katam:)")
# --------------------------daemon-------
from threading import Thread

def Display():
	print("Daemon Thread")
thread_1 = Thread(target=Display)
print("Before: ",thread_1.isDaemon())
thread_1.setDaemon(True) # wirte this method before start method
print("After: ",thread_1.isDaemon())
thread_1.start()
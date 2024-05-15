# ========================start() method===============
# start() - Once a thread is created it should be started by calling start() Method.
# Start the thread's activity.
# This method will raise a RuntimeError if called more than once on the
# same thread object.

from threading import Thread

def Marks():
	print("Marks")

M_1 = Thread(target=Marks)
M_1.start()
# M_1.start()  # error

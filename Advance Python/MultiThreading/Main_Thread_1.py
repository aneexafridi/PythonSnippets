# ===========main Thread===========
# main thread auto create when create any python program.
# and auto main thread start().

from threading import Thread

def Child_Thread():
	for u in range(3):
		print("Child Thread")
Child = Thread(target=Child_Thread)
Child.start()
# Note threads are not following the order
# the below code execute by seperately and the above also seperate
# that's why not follow the order
print()
for v in range(3):
	print("Main Thread")
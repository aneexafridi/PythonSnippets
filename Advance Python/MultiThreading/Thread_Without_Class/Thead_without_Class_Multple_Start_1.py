from threading import Thread
def Show_Roll(Roll):
	print("Threading is runing")
	print("Your Roll: ",Roll)

for u in range(5):
	Thread_object = Thread(target=Show_Roll,args=(38,))
	Thread_object.start()	# start() Method
	

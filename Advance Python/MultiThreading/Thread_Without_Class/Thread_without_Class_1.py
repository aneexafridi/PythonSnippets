# Creating Thead without a Class
# from theading import Thread
# Thread_object = Thead(target=function_name,arg=(arg=1,arg=n))
# Thread_object -> It represents our Thread.
# target - It represents the function on which the thread will act.
# args - It represents a tuple of arguments which are passed to the Fucntion.
#Example:===
			# Thread_object = Thead(target=Show_Roll(),args=(38,))
# ==================How to start Thead=====================
# Once a thread is created it should be started by calling start()
# Method.
# from threading import Thread
# def Show_Roll(Roll):
# 	print("Your Roll: ",Roll)
# Thread_object = Thread(target=Show_Roll,args=(38,))
# Thread_object.start()

from threading import Thread
def Show_Roll(Roll):
	print("Threading is runing")
	print("Your Roll: ",Roll)
Thread_object = Thread(target=Show_Roll,args=(38,))
Thread_object.start()# start() Method


		
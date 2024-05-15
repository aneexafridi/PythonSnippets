from time import sleep
from datetime import datetime

def Display(Time=None):
	if Time is None:
		Time = datetime.now()
	print(Time.strftime('%B %d %Y %H-%M-%S'))


# def Display(Time=datetime.now()):
# 	print(Time.strftime('%B %d %Y %H-%M-%S'))


Display()
sleep(1)
Display()
sleep(1)
Display()
sleep(1)
Display()
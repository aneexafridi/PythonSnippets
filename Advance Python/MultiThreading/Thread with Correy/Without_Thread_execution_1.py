from time import sleep,perf_counter

Start = perf_counter() # return float value

def Do_something():
	print("Sleeping for one 1 Seconds")
	sleep(1)
	print("Done Sleep....")

Do_something()
Do_something()

Finish = perf_counter()


print(f'Finish code {round(Finish-Start,2)} Seconds')


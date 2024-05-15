# -------------------Sleep() Mehtod
# This Mehtod is used to stop execution of a program temporarialy for
# a given amount of time. When this function is called, python virtual Machine(PVM)
# stops the program execution for given amount of time.
# Note_____ parameter must be in "Seconds" and non-negative
# It belongs to time module.

from time import sleep
#datetime module    time class
for u in range(1,11):
	print(u,end=' ')
	if (u==5):
		sleep(5) # sleep for 5 seconds
print()
List_1 = list([1,2,3,4])
print(List_1)
for u in List_1:
	if u == 3:
		sleep(2) # sleep for 2 seconds
	print(u,end=' ')
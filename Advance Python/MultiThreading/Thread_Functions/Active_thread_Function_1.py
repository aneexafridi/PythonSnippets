# ===================active_count() Method
# Return the number of Thread objects currently alive.
# The returned count is equal to the length of the list returned by enumerate().
# Note threads are not following the order
# the below code execute by seperately and the above also seperate
# that's why not follow the order


from threading import Thread,active_count



print("Main Thread")
print()

def Child_Thread():
		print("Child Thread")
Child = Thread(target=Child_Thread)
Child.start()

print("Total Threads in this program: ",active_count())

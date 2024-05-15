Name = None
try:
	Name = "Equal!=equal"
except Exception as e:
	raise
else: 	# else statement only execute when try passed then
	print(Name)
finally: # finall statement always execute
	print("\nFinally Statement")
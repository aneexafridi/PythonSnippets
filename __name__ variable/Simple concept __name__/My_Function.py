from time import sleep

def Loop_Function():
	for u in range(4):
		print('looping: ',u)
		sleep(0.8)
	print('End!!')

# Loop_Function()

if __name__ == '__main__':
	Loop_Function()

# for this statement we should must 
# call the function otherwise this
# will no execute because we just
# import the module
# if we don't use if __name__ variable
# then will import module auto call
# the function
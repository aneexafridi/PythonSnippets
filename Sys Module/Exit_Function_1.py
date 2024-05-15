# 				Exit Function
# exit() this function is used to terminate the execution or
# another words say exit the interpreter by raising SystemExit
# Syntax:-
 #      sys.exit(status=None,/)
 		# sys.exit() default set zero
 		# sys.exit(0) explicitly set zero
from sys import exit
# see help(exit)

for u in range(1,11):
	if u == 8:
		exit('\nTerminate')
	else:
		print(u,end=' ')

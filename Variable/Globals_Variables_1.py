# =======Global Variables
# when a Variable is declared above a function, it beccomes Global Variable.
# These Variables are available to all the function which are
# written after it.
# The Scope of global variable is the entire program body
# written below it.

Name = "Equal" # created Global variable
def Detail():
	your_Name = "equal" # created Local variable
	print("Local Variable",your_Name)
	print("Global Variable",Name) # use Global variable
Detail()
print("Global Variable",Name) # use Global variable
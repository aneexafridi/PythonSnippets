# --------------------fromkeys() Method
# this method is used to create a new dictionary with
# specified keys and values.
# Syntax:----
# 			dict.fromkeys(keys,value)
		# Note:-> dict is built-in
# Example:--
	# key = (1,2,3) # tuple
	# value = "Equal" # string
	# all key hold same value
	# Dict= dict.fromkeys(key,value)
	
key = (1,2,3)
value =['a','b','c']
print(value)

# for value parameter compiler set Default  None if not pass value
Dict = dict.fromkeys(key,value)
print(Dict)
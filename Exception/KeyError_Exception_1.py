# 					exception KeyError
# Raised when a mapping (dictionary) key is not found in
# the set of existing keys.

Dict = {'A':65,'B':66,'Z':90}

try:
	print(Dict['W'])
except KeyError:
	print('Sorry that does not exist in Dict')

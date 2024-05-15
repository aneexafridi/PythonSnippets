# 					exception FileNotFoundError
# Raised when a file or directory is requested but doesn’t exist.
# Corresponds to errno ENOENT.

try:
	f = open('MyFile.txt')
except FileNotFoundError as file_not_found_error:
	print(file_not_found_error)
else:
	print(f.read())
	f.close()

try:
	f=open('t.txt')
except FileNotFoundError as file_not_found_error:
	print(file_not_found_error)
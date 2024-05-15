# 				exception IndexError
# Raised when a sequence subscript is out of range.
# (Slice indices are silently truncated to fall in the
# allowed range; if an index is not an integer, TypeError 
# is raised.)

Tuple = (1,2,3)

try:
	print(Tuple[8])
except IndexError as index_error:
	print(index_error)
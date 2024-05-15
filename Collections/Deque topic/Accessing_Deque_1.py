from collections import deque

Deque = deque(['ali','Bilal','Shahab'],maxlen=3)
# by index access Deque

# deque.maxlen = is variable length of deque integer type

for u in range(Deque.maxlen):
	print(Deque[u],end=', ')

print()
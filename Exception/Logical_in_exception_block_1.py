A = 10
B = 0

try:
	C = A/B
except Exception as e:
	print(e)
	print('After handle program then default divide by one')
	C = A/1
	print(C)
else:
	print('Division: ',C)
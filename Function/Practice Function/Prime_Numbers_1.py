def Prime_Numbers(limit):
	diviser = 0
	for u in range(0,limit+1):
		for v in range(1,u+1):
			if u % v == 0:
				diviser += 1
		if diviser == 2:
			print(u,end=' ')
		diviser = 0
print('\n')
Prime_Numbers(15)
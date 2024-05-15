print("{0:*^30s}".format("Table"))
for m in range(1,11):
	for n in range(1,11):
		print("{0:2d}".format(m*n),end=" ")
	print()
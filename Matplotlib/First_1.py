from matplotlib import pyplot as plt

dve_x = [x for x in range(25,36)]

dve_y = [38496,42000,46752,49320, 53200,
		 56000,62316,64928,67317,68748,73752]

plt.plot(dve_x,dve_y,color='b',marker='o',label='Python')

plt.legend()
plt.show()
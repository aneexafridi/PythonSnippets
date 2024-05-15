from matplotlib import pyplot as plt

plt.xkcd()

Age = [12,18,21,24,28,30,38,41,49,55,59,61,71,77,81,95,100]

plt.hist(x=Age,range=(10,100),edgecolor='black',color='cyan',)

plt.xlabel('Age')
plt.ylabel('Total person')
plt.title('Programmers and Ages')
plt.show()
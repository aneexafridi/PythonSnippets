from matplotlib import pyplot as plt
from pandas import read_csv
from numpy import arange
plt.xkcd()
# File = read_csv(r'E:\Python in Sublime\Matplotlib\Sales_Records.csv'))

N = arange(1,10)
# M = arange(1,46).reshape(5,9)
# use M like or below the procedure
# plt.stackplot(N,M)
player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,1,1,2,2,2,2,3]
player3 = [1,1,1,2,2,2,3,3,3]
# M = [player1,player2,player3]
# plt.stackplot(N,M)

plt.stackplot(N,player1,player2,player3)


plt.tight_layout()

plt.show()
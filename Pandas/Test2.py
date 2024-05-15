from matplotlib import pyplot as py
from numpy import array
x = [1.,2.,5.,4.]
y = [11.,22.,33.,44.]
CA = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
CA.reverse()
py.scatter(x,y,s=200,marker='s',c=CA,edgecolor='black',linewidths=3,label='Box')
py.xlabel('X axis')
py.ylabel('Y axis')
py.title('Simple Chart')
py.legend()
py.show()
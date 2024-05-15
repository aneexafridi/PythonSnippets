from matplotlib import pyplot as pt
from numpy import arange
# print(pt.style.available)
# pt.style.use('fivethirtyeight')
# pt.xkcd(scale=-2,length=150,randomness=4)
pt.title('Languages')
x_1 = arange(1,10)
y_1 = arange(11,20)

pt.plot(x_1,y_1,color='Black',marker='o',markersize='8',linestyle='',label='Python')

pt.xlabel('X-axis',loc='center')
pt.ylabel('Y-axis',loc='center')

# which : {'major', 'minor', 'both'}, optional
# axis : {'both', 'x', 'y'},
pt.grid(color='blue',linestyle=':')
pt.legend(loc='upper left')
pt.show()
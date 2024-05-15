from matplotlib import pyplot as pt
from numpy import arange
# print(pt.style.available)
# pt.style.use('fivethirtyeight')
# xkcd(scale=1, length=100, randomness=2)
# pt.xkcd(scale=-2,length=150,randomness=4)
pt.title('Languages')
# 
x = arange(1,10)
y = arange(11,20)

pt.plot(x,y,'-b',linewidth=3,label='Python')

y = arange(5,14)
pt.plot(x,y,'--k',linewidth=2,label='Java')

pt.xlabel('X-axis')
pt.ylabel('Y-axis')

pt.grid(True)
pt.legend()
# pt.savefig('langge.png')
pt.show()
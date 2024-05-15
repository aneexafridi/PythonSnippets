from matplotlib.pyplot import plot,show
from numpy import arange

# help(plot) below code comment to see the plot function

x = arange(1,10)
y = arange(11,20)

plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+') 
show()
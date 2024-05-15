from matplotlib import pyplot as plt
from pandas import read_csv
from collections import Counter

DF = read_csv(r'E:\Python in Sublime\Matplotlib\Sales_Records.csv')

Item_Type = Counter(DF['Item Type'])

# plt.xkcd()
# Explode = [0,0,0,0,0.3,0,0,0,0,0.1,0,0.2]

plt.pie(x=Item_Type.values(),autopct="%1.2f%%",radius=1.1,labels=Item_Type.keys())

Textdict = {'fontsize':25,'color':'blue'}

plt.title(label='Items Sales',y=1,fontdict=Textdict)
plt.show()

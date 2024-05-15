from matplotlib import pyplot as plt
from pandas import read_csv
from collections import Counter

File = read_csv(r'E:\Python in Sublime\Matplotlib\Sales_Records.csv')

Count_item = Counter(File['Item Type'])

Sorted_Items = sorted(Count_item.items(),key=lambda x:x[1])


Item_sales = list(map(lambda x:x[0],Sorted_Items))
Sold = list(map(lambda x:x[1],Sorted_Items))

plt.barh(y=Item_sales,width=Sold)

plt.grid(axis='x')
plt.title('Sales Records',fontdict={"fontsize":20,'color':'red'})
plt.xlabel('Percentage Sales')
plt.show()
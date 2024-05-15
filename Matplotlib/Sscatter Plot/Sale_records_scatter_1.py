from matplotlib import pyplot as plt
from pandas import read_csv
File = read_csv(r'E:\Python in Sublime\Matplotlib\Sales_Records.csv')

plt.style.use('seaborn')
Total_Profit = File['Total Profit'].iloc[50:200] # 50 to 200
Units_Sales = File['Units Sold'].iloc[50:200]   # 50 to 200
Total_Cost  = File['Total Cost'].iloc[50:200]   # 50 to 200
Unit_Cost  = File['Unit Price'].iloc[50:200]    # 50 to 200



plt.scatter(x=Units_Sales,y=Total_Profit,
	s=100,marker='*',label='Unit sales',color='Green')

plt.scatter(x=Unit_Cost,y=Total_Cost,
	s=100,marker='*',label='Unit cost',color='blue')

# plt.xscale('linear')
# plt.yscale('linear')

Fontdict ={'fontsize':20,'color':'blue'}
plt.xlabel('Sales',fontdict=Fontdict)
plt.ylabel('Profit',fontdict=Fontdict)
plt.legend()
plt.title('Companies Profita and Sales',Fontdict)


plt.show()
from pandas import read_csv,to_datetime
from numpy import nan

Record = read_csv('1000 Sales Records.csv')
# 		 'Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority',
#        'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price',
#        'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit'

# Record['Ship Date'] = to_datetime(Record['Ship Date'])
# print(Record.loc[10,'Ship Date'].day_name())

from pandas import DataFrame
from numpy import nan



Dict = { "Name":["Zeeshan","Fawad","Bilal","Shahab",nan,nan,'Missing'],
		"Marks":[88,33,55,90,None,None,'Na'],
		"Address":["Peshawar","DI khan","Kohat","Dara Adam",None,nan,'Na']		
		 }
DF = DataFrame(data=Dict)
print(DF)
print()
print(DF.dropna())
print('\naxis = "index" and how = "any"')
print(DF.dropna(axis='index',how='any'))
print('\naxis = "columns" and how = "all"')
print(DF.dropna(axis='columns',how='all'))
from pandas import read_csv,DataFrame
from numpy import nan
Record = read_csv("pokemon_data.csv")
# ['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack',
#'Defense', 'Sp. Atk','Sp. Def', 'Speed', 'Generation', 'Legendary']
Filt = (Record['Legendary'] == nan)
print(Record[Filt])


# Dict = { "Name":["Zeeshan","Fawad","Bilal","Shahab",nan,nan,'Missing'],
# 		"Marks":[88,33,55,90,None,None,'Na'],
# 		"Address":["Peshawar","DI khan","Kohat","Dara Adam",None,nan,'Na']		
# 		 }
# DF = DataFrame(data=Dict)
# print(DF)
# print()
# print(DF.dropna())
# print(DF.types)

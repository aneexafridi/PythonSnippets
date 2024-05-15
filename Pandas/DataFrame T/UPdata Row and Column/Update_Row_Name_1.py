from pandas import DataFrame

Person = {
		"first_Name":['Ali','Fawad','Shahab'],
		"last_Name":['Zaman','Afridi','Afridi'],
		"marks":[11,44,55],
		"Email":['alizaman@gmail.com','fawadafridi@gmail.com','shahabafridi@gmail.com']
		}
DF = DataFrame(data=Person)
print(DF)
print('\n')
print(DF.index) # .index is attribute of DataFrame
print(DF.columns) # .columns is attribute of DataFrame
print('\n')
# use dictionary for a single column name or few or all
# then we should all index change and specify
# DF.index = ('a','b',2) 
DF.rename(index={0:'a',1:'b'},inplace=True)
# just changing the 0,1 index to a and b
print(DF)
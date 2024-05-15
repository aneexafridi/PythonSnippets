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
# DF=DF.drop(index=1)
# print(DF)
# -------------------------------------------------------------
# using filting # condition
filt = (DF['first_Name'] == 'Fawad') # return boolean Series
DF = DF.drop(index=DF[filt].index) #  DF[filt].index = only return index
print(DF)
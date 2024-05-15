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
# .index is attribute of DataFrame
print(DF.index) 
# .columns is attribute of DataFrame
print(DF.columns)
print('\n')
# for all columns name change then we should specify all the columns which are given in Dataframe
# DF.columns = ('first_Name','last_Name','marks','Email')
# for upper case fo columns
# DF.columns = [x.upper() for x in DF.columns] # DF.columns return the list of Columns

DF.rename(columns={'first_Name':"First",'last_Name':'last'},inplace=True)
print(DF)
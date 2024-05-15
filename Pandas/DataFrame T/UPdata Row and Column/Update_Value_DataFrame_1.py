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
#--------------------------------------------------------------------
# we just iloc method for index mean(row) then change all the values
# note all value should be specify whether you change or not
# DF.iloc[1] = ['Zeeshan','Khan',99,'zeeshankhan@gmail.com']
#-------------------------------------------------------------
# for changing single value then we should use built-in method at[]
# Access a single value for a row/column label pair.
# DF.at[1,'first_Name'] = "Zeeshan"
# ---------------------------------------------------------------------
# most commonly use the loc method
# DF.loc[1,'first_Name'] = 'Zeeshan' for single value
DF.loc[1,['first_Name','Email']] = ['Zeeshan','zeeshanafridi@gmail.com']
# for multiple value changing then use loc method
print(DF)
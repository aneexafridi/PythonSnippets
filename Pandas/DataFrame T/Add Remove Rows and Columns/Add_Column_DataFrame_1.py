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
print("\t\tAfter add the column of Full Name")
DF['Full_Name']=DF['first_Name'] + " " +DF['last_Name']
print(DF)
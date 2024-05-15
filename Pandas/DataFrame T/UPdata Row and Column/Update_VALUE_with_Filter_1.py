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
#  if firt_Name = 'Shahab' and last_Name = 'Afridi'
# then assign marks of that id = 55
# we can use for the filt 'and' keyword or some other 'or not'
Filt = ((DF['first_Name'] == 'Shahab') & (DF['last_Name'] == 'Afridi'))
# DF.at[Filt,'marks']= 99
DF.loc[Filt,['marks','first_Name']] = [99,'Equal']
print(DF)

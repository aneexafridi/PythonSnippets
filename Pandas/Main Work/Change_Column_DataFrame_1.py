from pandas import DataFrame

Person = {
		"first":['Ali','Fawad','Shahab'],
		"last":['Zaman','Afridi','Afridi'],
		"marks":[11,44,55],
		"Email":['alizaman@gmail.com','fawadafridi@gmail.com','shahabafridi@gmail.com']
		}
DF = DataFrame(data=Person)
print('\n\n')
print(DF)
# DF['first'] =  DF['first_Name']
DF.rename(columns={'fisrt':"First_Name",'last_Name'})
print(DF)
from pandas import DataFrame

Person = {
		"first_Name":['Ali','Fawad','Shahab'],
		"last_Name":['Zaman','Afridi','Afridi'],
		"marks":[11,44,55],
		"Email":['alizaman@gmail.com','fawadafridi@gmail.com','shahabafridi@gmail.com']
		}
DF = DataFrame(data=Person)
# we want to find the out where the first name is Shahab and the last name is Afridi

print(DF['first_Name']) # return just Series
print(type(DF['first_Name']))
print('\n\n')
Filt = ((DF['first_Name'] == 'Shahab') & (DF['last_Name'] == 'Afridi'))
# we can use for condition python keywords like 'and,or not'
# ---------------For negation we can use just '~' this sign before the Filt
# this will return all Emails except True
print(DF.loc[Filt,'Email'])

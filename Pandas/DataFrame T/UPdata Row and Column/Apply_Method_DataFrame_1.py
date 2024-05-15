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

print(DF['marks'].apply(lambda x:x*2))
# print(DF['first_Name'].apply(lambda U: U.upper()))

# --- Note
# if we want to replace the orignal data
# then use this way
# DF['marks'] = DF['marks'].apply(lambda x:x*2)
# DF['first_Name'] = DF['first_Name'].apply(lambda U:U.upper())
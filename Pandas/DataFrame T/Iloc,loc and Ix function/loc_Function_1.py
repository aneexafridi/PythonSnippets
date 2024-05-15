from pandas import DataFrame

# help(DataFrame.loc)

Person = {
		"first_Name":['Ali','Fawad','Shahab'],
		"last_Name":['Zaman','Afridi','Afridi'],
		"marks":[11,44,55],
		'Courses':('Python','HCI',"DATA"),
		"Email":['alizaman@gmail.com','fawadafridi@gmail.com','shahabafridi@gmail.com']
		 }

DF = DataFrame(data=Person,index=('one','two','three'))
print(DF)
print('\n\n')
print(DF.loc['one',['first_Name','marks']])
print(type(DF.loc['one',['first_Name','marks']]))
print('\n\n')
print(DF.loc[['one','two'],['first_Name','Courses','marks']])
print(type(DF.loc[['one','two'],['first_Name','Courses','marks']]))
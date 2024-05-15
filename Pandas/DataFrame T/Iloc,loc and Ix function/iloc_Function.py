# Purely integer-location based indexing for selection by position.
# .iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
# Allowed inputs are:

# An integer, e.g. 5.

# A list or array of integers, e.g. [4, 3, 0].

# A slice object with ints, e.g. 1:7.

# A boolean array.

# .iloc will raise IndexError if a requested indexer is out-of-bounds,
# except slice indexers which allow out-of-bounds indexing
# (this conforms with python/numpy slice semantics).


from pandas import DataFrame

Person = {
		"first_Name":['Ali','Fawad','Shahab'],
		"last_Name":['Zaman','Afridi','Afridi'],
		"marks":[11,44,55],
		'Courses':('Python','HCI',"DATA"),
		"Email":['alizaman@gmail.com','fawadafridi@gmail.com','shahabafridi@gmail.com']
		 }

DF = DataFrame(data=Person)
print(DF)
print('\n\n')
print(DF.iloc[1,[0,3]]) # 
# first [] cell for row and second is columns here we pass for columns
# print(DF.iloc[[1],[1,2]])

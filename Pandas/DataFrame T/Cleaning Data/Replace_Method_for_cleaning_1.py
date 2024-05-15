# i use replace method for none integer or float data type
from pandas import DataFrame
from numpy import nan

Dict = {
		"Names":['Shahab','Zeeshan','Alex','Bilal'],
		"marks":[50,55,nan,'Na']
		}
DF = DataFrame(data=Dict)
print(DF)
# if we find out  of the Marks the average or percentage then we will get Error
# because in marks column we have numpy num and String = 'Na'
# that's why we will no get the Average and some other calculation
# to do that we need to replace the Na String to zero 0
# and after that then we need to convert the datatype of the marks columns into float not to integer
DF['marks'].replace('Na',0,inplace=True)
DF['marks'].astype(float)
print()
print(DF)
print('\nMean "Average" of the marks')
print(DF['marks'].mean())
print('\nmedian "Percentage" of the marks')
print(DF['marks'].median())


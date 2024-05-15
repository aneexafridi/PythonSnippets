from pandas import DataFrame,read_csv

Dict = {"Name":["Alex","Bob","Jeo"],"Age":[10,20,30]}
print(Dict)
print("\n\n")

# Replace the column Names by Dictionary keys

print("Data Frame")
DF = DataFrame(data=Dict)
print(DF)
# print(DF.value_counts())
D =read_csv('Tep.csv')
print(D)
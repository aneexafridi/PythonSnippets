from pandas import DataFrame

Dict = {"Name":["Alex","Bob","Jeo"],"Age":[20,10,30]}
print(Dict)
print("\n\n")

# Replace the column Names by Dictionary keys

print("Data Frame")
DF = DataFrame(data=Dict)
print(DF)
print()
# median  method looking only numerical data in DataFrame not a String value
print("Median\n",DF.median())
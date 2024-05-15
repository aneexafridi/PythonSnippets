from pandas import DataFrame

Dict = {"Name":["Alex","Bob","Jeo"],"Age":[10,20,30]}
print(Dict)
print("\n\n")

# Replace the column Names by Dictionary keys

print("Data Frame")
DF = DataFrame(data=Dict,index=["Row1","Row2","Row3"])
print(DF)

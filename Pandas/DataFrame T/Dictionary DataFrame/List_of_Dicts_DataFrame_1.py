from pandas import DataFrame

List = [{'a':1,'b':2},{'a':11,'b':22,'c':33}]
print(List)
print("\n\n")

# Replace the column Names by Dictionary keys
# Not a Number (NaN) appended in missing areas.

print("Data Frame")
DF = DataFrame(data=List)
print(DF)

# Set Row 
print("Data Frame with rows")
DF = DataFrame(data=List,index=["Row1","Row2"])
print(DF)

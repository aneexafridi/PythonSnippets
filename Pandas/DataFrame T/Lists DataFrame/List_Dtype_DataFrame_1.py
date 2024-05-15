from pandas import DataFrame
List = [1,2,3,4]

print(List)
print()

DF = DataFrame(data=List,columns=['C1'])
print(DF)

print("\nAfter set the data type float")
DF = DataFrame(data=List,columns=['C1'],dtype=float)
print(DF)

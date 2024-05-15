# Drop method is used to for to drop row or column
# Syntax:
# 		DataFrame_name.drop(specfy Row or Column)

from pandas import DataFrame

# help(DataFrame.drop)

DF = DataFrame(data=((1,2,3),(4,5,6)),index=['row1','row2'],columns=['A','B','C'])
print(DF)

print("\nAfter using Drop method for row1")
DF=DF.drop(index=['row1']) # drop the row1 and remaining data assign to DF
print(DF)
print("\n")
print("After using Drop method for Column A")
DF =DF.drop(columns=['A'])
print(DF)
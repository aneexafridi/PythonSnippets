from pandas import DataFrame

# help(DataFrame.eval)

DF = DataFrame(data=((1,2),(3,4)),columns=('a','b'))
print(DF)
print('\n')
print("After we evalate the a and b then assigned to c")
print(DF.eval('c=a+b'))

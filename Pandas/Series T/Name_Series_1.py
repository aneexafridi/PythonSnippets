from pandas import Series
# The list method  return single character
print(list('abc'))

S = Series(data=(1,2,3),index=list('abc'))
# here we pass single character list to index
print(S)
print("The name of Series: ",S.name)
# now we set the name of Series
S = Series(data=(1,2,3),index=list('abc'),name="My First Series")
print("The name of Series: ",S.name)


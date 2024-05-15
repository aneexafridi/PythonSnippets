from pandas import Series
# help(Series.apply)

S = Series(data=(1,2,3,4),index=('a','b','c','d'))
print(S)

def Square(number):
	return number**2
print('\nAfter the Apply method')
# print(S.apply(func=Square))
# print(S.apply(func=(lambda x: x**2)))

# ------------------------------------------------------------------------
# Names = Series(data=('Shahab','Fawad','Zeeshan'))
# print(Names)
# print()
# print('After use the Apply method')

# # def Case_Upper(Word):
# # 	return Word.upper()
# # print(Names.apply(func=Case_Upper))

# print(Names.apply(func=lambda x: x.upper()))

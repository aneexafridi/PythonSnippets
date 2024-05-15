from pandas import array

Data = array(['11',99,'Shahab',True,3.5],dtype='object')
print(Data,'\n\n')
# uncomment the code below

# for  u in range(len(Data)):
# 	print(f'{Data[u]} Type {type(Data[u])}')

for u in range(len(Data)):
	if type(Data[u]) == int:
		print("Int Value: ",Data[u])
	elif type(Data[u])==str:
		print("Str Value: ",Data[u])
	elif type(Data[u])==bool:
		print("Bool Value: ",Data[u])
	elif type(Data[u]) == float:
		print("float Value: ",Data[u])
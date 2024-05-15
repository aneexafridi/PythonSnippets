from numpy import *
# Length = int(input("Enter length of Array: "))
 # create zeros string array
# Array = zeros(Length,dtype='<U20')#dtype = '<U20' mean take 20 character
# for u in range(Length):
# 	Array[u]=(input(f'{u}: Enter String: '))
# print(Array)

# using ones method same work as zeros method
Length = int(input("Enter length of Array: "))
#create ones string array
Array = ones(Length,dtype='U20')#dtype = '<U20' mean take 20 character
for u in range(Length):
	Array[u]=(input(f'{u}: Enter String: '))
print(Array)
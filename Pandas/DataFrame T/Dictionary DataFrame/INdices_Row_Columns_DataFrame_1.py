from pandas import DataFrame

List = [{"a":1,"b":2},{'a':11,'b':22,'c':33}]

print(List)
print()

DF1 = DataFrame(data=List,index=['First','Second'],columns=['a','b'])
DF2 = DataFrame(data=List,index=['Frist','Second'],columns=['a','c','d'])

print(DF1)
print()
print(DF2)
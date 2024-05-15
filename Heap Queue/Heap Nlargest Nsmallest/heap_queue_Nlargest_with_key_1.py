from heapq import nlargest

List = ['Fawad','Ali','Zeeshan','Shahab']

print(List)

Large_name = nlargest(2,List,key=len)

print(Large_name)
from heapq import nsmallest

List = ['Fawad','Ali','Zeeshan','Shahab']

print(List)

Large_name = nsmallest(2,List,key=len)

print(Large_name)
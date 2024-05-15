from operator import getitem

List = ['Ali','Fawad','Bilal','Shahab']
print(List)

# we want ot grab only Bilal and Shahab

print(getitem(List,slice(2,4)))
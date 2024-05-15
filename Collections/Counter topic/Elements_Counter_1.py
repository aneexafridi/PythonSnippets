# ------------------Element Method
#           elements()
# Return an iterator over elements "repeating" each as many
# times as its count. Elements are returned in the order 
# first encountered. If an element’s count is less than 
# one, elements() will ignore it.

# NOTE ---- Remove keys with 0 or negative value

from collections import Counter
				# create maping 
Counter_object = Counter(a=3,b=2,c=-1)
print(Counter_object)

Elements = Counter_object.elements()
print(tuple(Elements))
					#create  key argument
Counter_2 = Counter({'a':0,'b':2,'c':3})
print(Counter_2)
# print(list(Elements))
print(list(Counter_2.elements()))




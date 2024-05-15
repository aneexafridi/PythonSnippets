# Counter is a dict sub class that allows you to
# easily count objects. It has utility methods for
# working with the frequencies of the objects that
# you are counting

from collections import Counter
# a new, empty counter
c = Counter() 
print(c)
 # a new counter from an iterable
c = Counter('gallahad') 
print(c)
# a new counter from a mapping
c = Counter({'red': 4, 'blue': 2}) 
print(c)
# a new counter from keyword args
c = Counter(cats=4, dogs=8)  
print(c)
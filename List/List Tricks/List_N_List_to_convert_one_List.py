print()
List = [[1,2],[3,4],[5,6],[7,8],[9,10]]
print(List)
print(sum(List,start=[])) # Note i set to empty list []

print()
List = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(List)
print(sum(List,start=()))  # Note i set start to empty tuple ()
# also work on string like [['a'],['b']]

# help(sum)
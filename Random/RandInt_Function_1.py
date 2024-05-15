# -------- randint() method 
# randint use for integers
# this method have two formal arguments
# a = start limit , b  = end limit and both included a,b
from random import*
for u in range(5):
	print(randint(1,10),end=' ')

print()
List_Compre = [randint(1,10) for u in range(5)]
for u in List_Compre:
	print(u,end=' ')
# Arrays can store only one Type of data
# ----Note----
# In Python, The size fo Array Is Not fixed.
# Array can increase Or decrease their size dynamically.
# In Python, Multi-Dimensional Array Not support
# Array And List are Not Same
# Array use less memory than List
#typecode must be (b,B,u,h,H,i,I,l,L,q, Q, f or d)
from array import*
Array = array('i',[1,2,99,4])
for u in range(len(Array)):
	print(Array[u],end=' ')
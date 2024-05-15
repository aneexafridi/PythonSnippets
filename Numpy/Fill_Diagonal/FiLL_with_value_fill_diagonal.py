from numpy import arange,fill_diagonal

# help(arange)
# help(fill_diagonal)

Arange  = arange(1,10).reshape(3,3)
#  reshape is attribute of numpy

print(Arange) # arange method
print("_"*20)

fill_diagonal(a = Arange,val = 0) # remember fill_diagonal function nothing return

# parameter of fill_diagonal
# a = must be n-darray atleast 2-d array
# val can be any digit mean nagetive or positive or array

print(Arange)

from numpy import ones , fill_diagonal

# help(ones)
# help(fill_diagonal)

Z = ones(shape=(4,4),dtype=int)
print(Z)
print('*'*20,'Ones\n')

fill_diagonal(a=Z,val = 0) # remember fill_diagonal method nothing return

# a = must be n-darray atleast 2-d array
# val can be any digit mean nagetive or positive

print(Z)

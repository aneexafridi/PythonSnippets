from numpy import zeros , fill_diagonal

# help(zeros)
# help(fill_diagonal)

Z = zeros(shape=(4,4),dtype=int)
print(Z)
print('*'*20,'Zeros\n')

fill_diagonal(a=Z,val = 9)  # remember fill_diagonal method nothing return

# a = must be n-darray atleast 2-d array
# val can be any digit mean nagetive or positive

print(Z)

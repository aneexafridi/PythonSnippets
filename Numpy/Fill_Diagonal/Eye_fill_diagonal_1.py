from numpy import eye , fill_diagonal

# help(eye)
# help(fill_diagonal)

# eye method return the identity matrix
E = eye(N=3,M=3,dtype=int)
print(E)
print('*'*20,'identity\n')

fill_diagonal(a=E,val = 9)
# E = eye(N=3,M=3,dtype=int) * 9 # same
# remember fill_diagonal method nothing return

# a = must be n-darray atleast 2-d array
# val can be any digit mean nagetive or positive

print(E)

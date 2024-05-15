# ----------------------Eye Function
# >> This Function is used for identity matrix
# N = row Must
# M = column optional if we don't  give then by default
# set M = "N"
# help(eye)

from numpy import eye

print(eye(N=3,M=3,dtype=int))
# Same as above code
print("\n\n")
print(eye(N=3,dtype=int))
print('\n')
# Same as above code
print(eye(3,dtype=int))


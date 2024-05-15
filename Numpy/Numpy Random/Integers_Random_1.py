from numpy.random import randint

# help(random.randint) particular the parameter
# -> See the parameters of random.randint

R = randint(low=10,high=15,size=(3,3))
print(R)

# range is low to high
# NOTE ----
# low included  and high excluded # [low,high)
# size default None  can passing tuple (m,n,k)

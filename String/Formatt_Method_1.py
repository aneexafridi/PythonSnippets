# format() is built-in  method 
# syntax  {index/key:[fill][align][sign][#][0][width][,][.precision]type}
print("Name is{}".format("Equal!=equal"))
print("{0}{1}".format(1,2))
print("{1}{0}".format(1,2))
print("{M}{N}".format(M=9,N=8))
# ------ 
print("{0:10d}".format(100))
print("{0:13.2f}".format(100.1234))
print("{0:05d}".format(10))
print("{0:*<10d}".format(10))
print("{0:*>10d}".format(10))
print("{0:^10d}".format(10)) # give centre
print("{0:*^10d}".format(10))
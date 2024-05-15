from time import time,ctime,localtime
epoch  = time() # epoch mean start time
print(epoch)

convert_Time = ctime(epoch)
print(convert_Time)
print(ctime())
Lt = localtime()
print(Lt.tm_time)
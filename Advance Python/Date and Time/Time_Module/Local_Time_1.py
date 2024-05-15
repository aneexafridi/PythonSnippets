# localtime() Fucntion - This function is used to convert seconds into date and
# time. It returns an object struct_time Which can be used to access the
# attributes either using an index or using a name.

from time import *
# ctime() function return current date and time
# if we pass specific formal argument then return
print(ctime())

Current_Time=  localtime()
print("Year: ",Current_Time.tm_year)
print("Month: ",Current_Time.tm_mon)
print("Date: ",Current_Time.tm_mday)
print("Hour: ",Current_Time.tm_hour)
print("Minute: ",Current_Time.tm_min)
print("Second: ",Current_Time.tm_sec)

print("attributes of localtime Fucntion")
print(Current_Time)

print("Time format")
print(f'{Current_Time.tm_hour}:{Current_Time.tm_min}:{Current_Time.tm_sec}')
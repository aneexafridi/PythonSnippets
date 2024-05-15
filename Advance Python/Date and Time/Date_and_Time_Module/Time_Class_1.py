# --------------------time Class
# time object - A time object is an object containing information of local time
# of day, independent of any particular day,and subject to adustment via a
# tzinfo object.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # creating object of time Class
# object_name = time(hour=0,minute=0,second=0,microsecond=0,tzinfo=None,*,fold=0)
# All arguments are optional.tzinfo may be None, or an instance of tzinfo subclass.
# The remaining arguments may be integers, in the following ranges:
# 0 <= hour<24
# 0 <=minute < 60
# 0<=second < 60
# 0 <=microsecond < 100000,
# fold in [0,1]
# all default to 0 except tzinfo, which default to None.
# Example: t = time(hour =5,minute=34,second=44)
from datetime import time
t = time(hour=12,minute=4,second=55)
print(t)
print(t.hour)
print(t.second)








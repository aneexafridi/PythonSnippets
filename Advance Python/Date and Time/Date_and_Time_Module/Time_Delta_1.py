# -------------------timedelta Class------------------
# timedelta Object - A timedelta object represents a duration, the difference between two dates or times.
# ---------------------------------------------------------------------------------------------------------
# -------creating object of timedelta Class
# object_name = timedelta(days=0,second=0,microseconds=0,milliseconds=0,minutes=0,
# 	hours=0,weeks=0)
# all arguments are optional,
# and default set 0, arguments may be integers or flaats and positive or negative.
#---------------------------------------------------------------------------------
# when we use timedelta Class 
# if we subsribe the service after ten or some days will be exprire
from datetime import timedelta,date
Today = date.today()
print(Today)
Time_Delta = timedelta(days=10)
print(Time_Delta)
print(Time_Delta+Today)
Time_Delta = timedelta(days=14)
print(Today-Time_Delta)
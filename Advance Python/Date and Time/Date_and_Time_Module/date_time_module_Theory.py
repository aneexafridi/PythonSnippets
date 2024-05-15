# ---------------------------------datetime Module
# datetime -It handles date and time. It has year, month,day,hour,minute,
# second,micosecond and tzinfo attributes.

# date -- It handle dates of greporian calendar, without taking time zone
# into consideration. it has year,month and day attributess.

# time-- It handles time assuming that every day has exactly 24 x 60 X 60
# seconds. It has hour,minute,seconds,micosecond and tzinfo attributes.

# timedelta  -It handles duartions. The duartion many be the difference
# between two date,time or datetime instances.
#______________________________datetime class___________________________
# datetime object - A datetime object is a single object containning all
# the information from a date object and a time object.
# >>> create object
# object_name = datetime(year,month,day,time_attributes)
# but year month and day must pass as argument
# Minyear <= year <= Maxyear
# 1 <= month <= 12
# 1 <=day<=number of days in the given month and year

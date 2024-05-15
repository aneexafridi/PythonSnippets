# --------------------------date Class
# date object - A date object is an object containing information of
# year,month and day.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# creating object of date Class
# object_Name  = date(yaer,month,day)
# all arguments are required. Arguments may be integer, in the
# following ranges:
# MINyear <=year<=MAXyear
# 1 <=month<=12
# 1 <= day<=number of days in the given month and year
# Ex: 
# d = date(year=2021,month=3,day=12)
from datetime import date
print(date(2021,3,12))  
Date = date(2022,5,23)
print(Date.year)
print(date.today().year)
print(date.today().day)
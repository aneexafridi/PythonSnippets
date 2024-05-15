# ----------------Comparing Two Dates
# We can compare date Class and datetime Class objects using ==,<,>.
# The Comparison will return either True or False.
from datetime import date
Date_1 = date(year=2019,month=6,day=30)
Date_2 = date(year=2021,month=3,day=13)
print(Date_1==Date_2)

Date_11 = date(1990,5,9)
Date_22 = date(2000,4,3)
print(Date_11==Date_22)
print(Date_1<Date_2)
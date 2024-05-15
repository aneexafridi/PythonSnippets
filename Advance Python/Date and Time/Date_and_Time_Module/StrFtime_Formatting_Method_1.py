# -----------------Formatting Date and Time
# strftime() Method - This method is used to format the content of datetime,
# date and time Class Object. strftime repesents string fromat to time.
# This method convert the Object inot a specific format and returns the 
# formatted string.
# Example:---
# 		Date = datetime.today()
#       Format_date = Date.strftime("%B ,%d , %Y")


from datetime import datetime
Date = datetime.today()
print(Date)
print(Date.strftime("%B,%d %Y"))
# For Time
Time = datetime.today()
print(Time)
print(Time.strftime("%I:%M:%p"))
print(Time.strftime("%I:%M:%S:%p"))

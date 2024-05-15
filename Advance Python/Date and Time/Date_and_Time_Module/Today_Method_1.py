# ----------------------------today() method
# today() - This method is used to get the current date and time.
# It returns the date and time information.

from datetime import datetime
print(datetime.today())
# we can access single attribute of datetime
print(datetime.today().year)
print(datetime.today().day)
print(datetime.today().minute)
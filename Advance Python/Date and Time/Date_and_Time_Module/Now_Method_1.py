# --------------------------now() Method
# now() -- This method is used to get the current date and time.We can provide timezone
# information to this method.If the timezone is not porvided, thenit takes the local time
# zone. It returns an object that contains date and time information in any timezone.
# We can use day,month,year,hour,minute and second.
# Example:---- datetime.now()
from datetime import datetime
print(datetime.now())
# we can access single attribute of datetime
print(datetime.now().year)
print(datetime.now().day)
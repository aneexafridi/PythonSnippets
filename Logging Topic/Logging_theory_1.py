# -------------------Logging 
# Logging is useful to track the error or exception or information.
# It also helps in debugging.

# we use logging module to log the error

# Syntax:-
# 		from logging import *,,,,


from logging import *

debug('This is debug') # low level
info('This is info') # low level
warning('This is warning') 
error('This is error')
critical('This is Critical')
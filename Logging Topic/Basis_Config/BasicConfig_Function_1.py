# -------------------BasicConfig Function
# basicConfig(**kwrargs) This function is used to config the logging system.

# parameters:
# >> filenmae - It specifies that a fileHandler be created,using the specified filenmae,
# rather than a StreamHandler.
# >> filemode f filename is specified, open the file in this mode. Defaults to 'a'. We
# can write mode 'w'

# >> level - Set the root logger level to the specified level.
# >> format - Use the specified format string fro handler.

# Level  		= Numeric value

# CRITICAL        50
# ERROR           40
# WARNING         30
# INFO 			20
# DEBUG           10
# NOTSET          0




from logging import *

basicConfig(filename='Logfile.log',level=DEBUG,filemode='w')

debug('This is debug')
info('This is INFO')

warning('Thsi is warning')
error('This is error')
critical('This is critical')

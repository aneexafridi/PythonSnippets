# ----------- Keyword-Only Arguments
# To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument,
#  place an * in the arguments list just before the first keyword-only parameter.


def Keyword_only_arg(*,arg):
	print(arg)


Keyword_only_arg(arg='Equal')
# Keyword_only_arg('equal') # will give Error
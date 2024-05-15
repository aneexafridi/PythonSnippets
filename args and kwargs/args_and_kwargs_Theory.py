# There a few things to Note:
# >> The names args (arguments) and kwargs(keywordargument)
# are used by convention, they are not a part of the language
# specification.Thus, these are equivalent:
# args return tuple and kwargs return Dictionary


# Def Fun(*args,**kwargs):
# 	print(args)
# 	print(kwargs)
# Def Fun(*a,**b):
# 	print(a)
# 	print(b)

# -------------------Note--------------------------------
# you may not have more than one args or more than one
# kwargs parameters(however they are not required)
# **kwargs must come last in the parameter list.
# error  def fun(*arg1,*args2) == invalidSyntax
# error def fun(**kwargs,*args) == invalidSynatx
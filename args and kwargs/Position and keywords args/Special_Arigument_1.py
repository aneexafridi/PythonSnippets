# --------------Special parameters
# By default, arguments may be passed to a Python function either by
# position or explicitly by keyword. For readability and performance,
# it makes sense to restrict the way arguments can be passed so that a
# developer need only look at the function definition to determine if 
# items are passed by position, by position or keyword, or by keyword.

# A function definition may look like:

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only



def Fun(pos1,pos2,/,pos_or_kwd,*,kwd1,kwd2):
	print('pos: ',pos1,pos2)
	print("pos_or_kwd: ",pos_or_kwd)
	print("kwd: ",kwd1,kwd2)


Fun(1,2,pos_or_kwd='pk',kwd1=11,kwd2=22) 
print('\n')
Fun(11,22,'pk',kwd1=1,kwd2=2)
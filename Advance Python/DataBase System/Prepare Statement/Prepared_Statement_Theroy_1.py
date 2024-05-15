# ---------------Prepared Statement

# A Prepared Statement is used to execute the same statement repeatedly with
# high efficiency. The Prepared statement execution consists of two stages:
# prepare and execute.

# at the prepare stage a statement template is sent to the database server.
# The server performs a syntax check and initializes server internal resources
# for later use.
# Al the exeecute stage the parameter values are sent to the server.
# The server creates a statement from the statement template  and
# these values to exeecute it.
# prepared statements exeecuted with MySQL CursorPrepard can use format %s or
# qusetion ? mark parameterization style.

# %s and ? are called as parameter marker.
# This differs from nonprepared statements exeecuted with MySQL Cursor,
# which can use the format or pyformat parameterization style.

# ______________________________________________________________________________
# ---------------------Advantage---------------------------

# >> prepared statements are very useful against SQL injections.
# >> prepared statements reduce parsing time as the preparation on the query
# is done only once (although the statement is executed multiple times)
# ------------------------------------------------------------------------------
# -------------------------Creating a Cursor
# cursor(prepard=True) return cursor object



# Note ------ for qurery only use tuple



# syntax:-
		# Cursor_object = Connect_object.cursor(prepared=True)
		# sql = 'insert into student(name,roll) values(?,?)'or values(%s,%s)
		# Cursor_object.execute(sql,('name',22))


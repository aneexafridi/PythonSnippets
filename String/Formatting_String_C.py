# C-Style String Formatting
# % operator/Modulo Operator/Interpolation Operator
# this operator is used for formatting strings.
# It interprets the left argument much like a 
# sprintf() style format string to be pplied to
# the right argument, and returns the string
# resulting from this fromatting operation.
# Syntax:- print("Format placeholder"%(data))
Name = "Equal!=equal"
print("%s"%(Name))
# placeholder or specifier = %[flags][width][.precision]tye
# Note Width work only if width is Great>string characters
print("%24s"%(Name))
print("%.2f"%3.1445)
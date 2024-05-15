# ------reduce() Function
# This function is used to reduce a sequance of 
# Elements to a single value by processing the elements
# according to function supplied.
# It returns a single value.
# This function is a part of "functools" module so you
# have to import it before using.
# Syntax:---
# 		From functools import reduce
# 		reduce(function_Name,sequance_name)

from functools import reduce # instead use reduce *
List = ['E','q','u','a','l']
print(List)
Result = reduce(lambda u,v:(u+v),List)
print(Result)
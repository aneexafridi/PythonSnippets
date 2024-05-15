# -----------------Module
# A module is a file containing Python definitions and statements.
# A Module is file containing group of vairables,methods,function
# and Classes etc.
# They are executed only the first time the module
# Name is encountered in an import statement.
# The file name is the module name with the suffix.py appended.
# Ex:--
#      MyModule.py
#----------------------------------------------------------------
# -----Very Important  The Project folder Name have not space
#_________________________________________________________________
# Type of Module:----
# >> User-defined Modules
# >> Built-in Modules
# Ex:---- array,math,numpy,sys
# User-defined Modules
# User-defined Module in we need to create  module
# after then import that module
# Built-in Module we don't need to create module
# we just import the module

# When and Why use Module
# +++++++++++++++++++++++++++++
# Assume that you are building a very large project, it will be very
# difficult to manage all logic within one single file so if you
# want to separate your similar logic to a separate file, you can
# use module.
# it will not only separate your logics but also help you to debug your
# code easily as you know which logic is defined in which module.
# When a module is developed,it can be reused in any program that needs
# that module.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# How to use Module
# import statement is used to import modules.
# Syntax:-- import module_Name
		    # import module_Name as alias_name
		    # from module_Name import  function1,function2,function_N
		    # from module_Name import variable1,variable2,variable_N
		    # from module_Name import class_1,class_2,Class_N
		    # from module_Name import Class_Name,Dictionay,function,List,ete
		    # from module_Name import as alias_name
		    # from module_Name import * # * means all import in module_Name file
		   # Note---------- Modules can import other modules.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# --------------------Import module name
# This does not enter the names of hte functions defined in module directly in the
# current symbol table; it only enters the module name there.
# Example:-- import module_Name
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# How to access Methods,Functions,Variables and Classes?
# using the module name you can access the functions,or etc.
# Syntax:-- module_Name.function_Name()
# Example:- Addion.add(1,2)
# shortcut is A = Additon.add then A(1,2)
# When 2 modules having same functions name then This import module is
# good approach to use.

# --------------------------Package
# Packages are a way of structuring python's Module namespace by
# using "dotted module names".

# A Package can have one or more modules which means,a Package is
# collection of modules and Packages.
# A package can contain packages.
# Package is nothing but a Director/Folder
# ----------------------------------------------------------------
# --------------------Creating Package
# Package is nothing but a Directory/Folder which Must contain a 
# special file called __init__.py.
# __init__.py file can be empty, it indicates that the Directory
# it contains is a python package, so it can be imported the same
# way a module can be imported.
# ----------------------------------------------------------------
# --------------------How to use Package
# Syntax:- import packageName.module_Name
# Syntax:- import packageName.subPackage_Name.module_
# ----------------------------------------------------------------
# -------------How to use Package
# Syntax:- from packageName import module_Name
# Syntax:- from packageName.subPackage_Name import module_Name
#--------------------Note
# Syntax:- from packageName import Module_Name * will not work
#---------------------------------------------------------------
# -------------------- __all__() Methdo
# if a package's __init__.py code defines a list named __all__,
# it is taken to be the list of modules Names that should be
# imported when from package import * is encountered.
#Example  __all__ = ["Module_1","module_2","module_3"]

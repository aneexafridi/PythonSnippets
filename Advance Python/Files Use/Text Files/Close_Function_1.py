# -------------Closing a File
# close() This method is used to close,opened file.
# Once we close the file, file object is deleted from the memory hence file will be 
# no longer accessible unless we open it again.
# If you don't explicitly close a file Python's garbage collector will eventually
# destroy the object and close the open file for you,but the file may stay open for 
# a while so You should always close opened file.
# ====================================================================================
# What wil happened if we do not close opened file:--
# >> Data of the may be corrupted or deleted.
# >> Memory utilized by the file is not freed it may cause of insufficient memory.


# f = open("Student.txt")
# help(f.close)
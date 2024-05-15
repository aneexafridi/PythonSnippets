# ------------------Files
# File is the collection of data that is available to a program.
# we can retrieve and use data stored in file whenever we required.
# ==================================================================
# Advantages:
# >> Stored Data is permanent unless someone remove it.
# >> Stored data can be shared.
# >> It is possible to update or remove the data.
# ====================================================================
# ----------------------------Type of Files
# There are two type of files:
# 1 >> one is  Text File - It stores data in the form of characters.
# It is used to store characters and strings.

# 2 >> second one is Binary File - It stores data in the form of bytes,
# a group of 8 bits each,It is used to store text,images,pdf,csv,video,and audio.

file = open("Student.txt",mode='w')
file.write("my Name is Equal!=equal")
file.close()
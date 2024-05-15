# --------------- Text File Mode
# r = Open for reading. The file pointer is positioned at the beginning of the file.
#     If the file doesn't exist it will show FileNot FoundError.

# w = Open for writing. If data is already present in the file, it will overwrite the
#     data.If the file does't exit it will create that file.
#     pointer is beginning in w mode

# x = Open for exclusive creation with write.The specified file must not be available.If
#     the specified file is available it will show error FileExistsError

# a = Open for appending. The file pointer is positioned at the end  of the file.
#     It appends new data at the end of file.If the file does not exist it will create a new file
#     for writing data.

# r+ =  Open for reading and then writing.

# w+ = Open for Writing and then reading.It will overwrite existing data.

# a+ = Open for appending then reading. It won't overwrite existing data.

# ==================================================================================
#   mode= 'w+'
# Writing and then reading It will overwrite existing data
file = open("Student_Method.txt",mode='r+')
file.write("Use Write method")
file.seek(0)
print(file.read())
file.close()
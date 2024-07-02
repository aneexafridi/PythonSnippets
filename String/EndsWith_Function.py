# endswith() This method is used to check whether a
# string is ending with a substring or not.
# It returns True If string ends with specified sub string.
# Syntax:- string.endswith("specified string")
Line = "Hi this is Equal .txt"
print(Line)
print(Line.endswith("Equal"))
print(Line.endswith("equal"))
if Line.endswith(".txt"):
    print("txt")
else:
    print("ok")
# Python can look for extra whitespace on the right sides
# of a string. To ensure that no whitespace exists at the right end
# of a string, use the rstrip() method.

Name = "Shahab "
print(len(Name))
print(Name)
Name = Name.rstrip() # this code as Same  Name = " Shahab".rstrip()
print(len(Name))
print(Name)
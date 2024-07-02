# Python can look for extra whitespace on the left sides
# of a string. To ensure that no whitespace exists at the left end
# of a string, use the lstrip() method.

Name = " correct"
print(len(Name))
print(Name)
Name = Name.lstrip() # this code as Same  Name = " Shahab".lstrip()
print(len(Name))
print(Name)
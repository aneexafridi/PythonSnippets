
from random import choices

# help(choices)

Colors = ['white','black']

Choices = choices(population=Colors,weights=[90,10],k=3)
print(Choices)


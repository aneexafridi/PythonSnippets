from pandas import DataFrame
from numpy import nan

DF= DataFrame({"Person":["John", "Myla", nan, "John", nan],
                "Age": [24., nan, 21., 33, 26],
                "Single": [False, True, True, True, False]}
                )

print(DF)

print('\n')
print(DF.count())

# nan can not count the count method
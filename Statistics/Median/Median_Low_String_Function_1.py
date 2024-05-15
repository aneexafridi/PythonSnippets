from statistics import median_low
from string import ascii_uppercase 
# ascii_uppercase is variable in string module which is assigned A to Z
# help(median_high)
# List = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']
List = [ascii_uppercase[u] for u in range(8)]

print(List)

print(f'Median low: {median_low(List)}')

# also same work for Integers

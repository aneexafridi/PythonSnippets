# fmean(data)
# Convert data to floats and compute the arithmetic mean.

from statistics import fmean
from numpy import arange

List = arange(1,6,dtype=float)
print(List)

print(f'Average of float: {fmean(List)}')
from statistics import median

# help(median)
List = ['a','b','c','d','e','f','g']
print(List)
print(f'median: {median(List)}')


print()
List = ['a','b','c','d'] 
# this will give TypeError because  if iterable is even length then 
# average of two madian, if it is  string then average does not work
#------------------- in Integer will work
# ----to recommend  use median_high or median_low

print(f'median: {median(List)}')


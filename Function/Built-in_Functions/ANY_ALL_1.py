# help(all)
# help(any)

# for any() al least one true
# for all all should be true

x = [True, True, True]
print(x)
if any(x):
    print("At least one True (any)")
if all(x):
    print("Not one False (all)")
if any(x) and not all(x):    
    print("At least one True (any) [and] one False (all)")
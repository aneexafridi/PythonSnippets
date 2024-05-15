# syntax  {index/key:[fill][align][sign][#][0][width][,][.precision]type}
# F or f
Name = "Equal!=equal"
print(f"My Name is {Name}")
print(f"My Name is {Name.upper()}")
M = 1
N = 2
print(f"{M}{N}")
print(f"{N}{M}")
# ------
F = 3.14555 
print(f"{N:10d}")
print(f"Floating points: {F:.2f}")
print(f"{N:13.2f}")
print(f"{N:05d}")
print(f"{N:*<10d}")
print(f"{N:*>10d}")
print(f"{N:^10d}") # give centre
print(f"{N:*^10d}")
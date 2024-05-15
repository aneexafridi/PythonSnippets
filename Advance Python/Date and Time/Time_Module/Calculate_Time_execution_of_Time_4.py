from datetime import datetime

begin_time = datetime.now()
print(begin_time)

[4, 2, 3, 1, 5].sort()
[4, 3, 6, 1, 2].sort()
[4, 2, 5, 1, 3].sort()

for u in range(30):
	print(u,end=' ')
# print(datetime.now())
print()

print(datetime.now() - begin_time)
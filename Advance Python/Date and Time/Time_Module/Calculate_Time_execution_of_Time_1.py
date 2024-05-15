from time import time,sleep
# importing  time() and sleep() methods from time module

# starting time
Start = time()

# program body starts
for u in range(10):
    print(u,end=' ')

# sleeping for 1 sec to get 10 sec runtime
sleep(1)

# program body ends

# end time
End = time()
print('\nCalculate: ',End-Start)
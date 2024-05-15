from collections import deque

# once we decleare the maxlen of the deque then if the deque is full
# then if we use append will remove the first element then insert
# else if we use appendleft will remove the last element then insert
# auto then append

Deque = deque([1,2,3,4],maxlen=4)
print(Deque)

print('After add another element')
Deque.append(5)
# Deque.appendleft(5) # check by one by one appendleft
print(Deque)


# ----------------Note-------------
# >> 1 see the heap module
# >> 2 and also see the Queue module
from threading import current_thread

print(current_thread().getName())
print(current_thread().isDaemon())
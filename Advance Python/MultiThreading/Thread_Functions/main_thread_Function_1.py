# ================main_thread() Function
# Return the main Thread object. In normal conditions, the main
# thread is the thread from which the Python interpreter was started.
from threading import main_thread

print(main_thread())
print()
print(f"Name of the Thread is:  [{main_thread().getName()}]")
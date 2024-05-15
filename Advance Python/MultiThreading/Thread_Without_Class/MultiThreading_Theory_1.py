# ========================Multithreading==============
# using Multiple Threads in program or process
# >> Multimedia Graphic
# >> Animations
# >> Video Games
# >> Web Servers
# >> Application Servers

# ------------------------Thread--------------------
# Thread is a seperate flow of executiiion.Every thread has a task.
# _________________________________________________________________
# =======================Main Thread==============================
# When we start any python program, one thread begins running
# immediately, which is calledd Main Thread of that program created by PvM.
# The Main thread is created automatically when your program is started.

import threading  # Module name threading
Main_Thread=threading.current_thread().getName()
print("Equal!=equal")
print(Main_Thread)

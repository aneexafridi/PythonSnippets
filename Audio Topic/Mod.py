# import vlc
# p = vlc.MediaPlayer("This_is_a_Jazz_Space.mp3")
# p.play()


# p.stop()

# from time import *
# from sys import exit
# from datetime import time
# import playsound

# P = playsound.playsound('This_is_a_Jazz_Space.mp3',True)
# print('p')



from audioplayer.audioplayer_windows import*
from sys import exit
Track = AudioPlayerWindows('This_is_a_Jazz_Space.mp3')
while True:
	c = input('''
		Enter py: for play
		Enter p: for pause
		Enter r: for resume
		Enter s: for stop
		Enter q: for quit\n>> ''')
	if c == 'py':
		t.play(block=True)
	elif c == 'p':
		t.pause()
	elif c == 's':
		t.stop()
	elif c == 'q':
		exit(1)
	else:
		print("Invalid")
t.close()
















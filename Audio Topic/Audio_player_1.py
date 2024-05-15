# package audioplayer sub-package audioplay_windows
from audioplayer.audioplayer_windows import*
from sys import exit

# help(AudioPlayerWindows)
# all methods


# Track = AudioPlayerWindows('This_is_a_Jazz_Space.mp3')
Track=AudioPlayerWindows('khumariyaan.mp3')
Track.volume = 50              # volume range(0-100)
while True: 	
	print(f'Track Name: "{Track.filename}"')
	choice = input('''
		Enter py: for play
		Enter p:  for pause
		Enter s:  for stop
		Enter r:  for resume
		Enter q:  for quit\n>> ''')
	if choice == 'py':
		Track.play()
	elif choice == 'p':
		Track.pause()
	elif choice == 's':
		Track.stop()
	elif choice == 'r':
		Track.resume()
	elif choice == 'q':
		print(f'Track Name: "{Track.filename}"')
		exit()
	else:
		print("Invalid")

Track.close()
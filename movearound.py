from curses import wrapper
import curses
import pdb

def main(stdscr):
	stdscr.clear()
	#stdscr.keypad(False)
	stdscr.box()
	#stdscr.curs_set(0)
	y = 9
	x = 11
	#loop = True

	while True:
		key = stdscr.getkey()
		if key == 'q':
			return
		stdscr.addch(y, x, ' ')
		y, x = move(key, y, x)
		stdscr.addch(y, x, '&')
		stdscr.move(y, x)

def move(key, y, x):
	if key == 'KEY_DOWN':
		y+=1
	elif key == 'KEY_UP':
		y-=1
	elif key == 'KEY_LEFT':
		x-=1
	elif key == 'KEY_RIGHT':
		x+=1
	return y, x

wrapper(main)

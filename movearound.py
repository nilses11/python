from curses import wrapper
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
import pdb

y = 9
x = 11
loop = True
hasChanges = False
dirt = []
maxyx = []

def main(win):
	global maxyx
	win.box()
	maxyx = win.getmaxyx()
	try:
		win.curs_set(0)
	except:
		pass
	#Set start position
	win.addch(y, x, '&')
	win.move(y, x)
	
	while loop:
		key = win.getkey()
		win.addch(y, x, ' ')
		if key in keymappings:
			keymappings[key]()
		if hasChanges:
			doChanges(win)
		win.addch(y, x, '&')
		win.move(y, x)

def quit():
	global loop
	loop = False

def moveup():
	global y
	y-=1

def moveleft():
	global x
	x-=1

def moveright():
	global x
	x+=1

def movedown():
	global y
	y+=1

def generateDirt():
	global dirt
	global hasChanges
	hasChanges = True
	for yes in range(maxyx[0]-15):
		line = ''
		for xes in range(maxyx[1]-2):
			line+='#'
		dirt.append(line)

def doChanges(win):
	global hasChanges
	global dirt
	for i in range(len(dirt)):
		line = dirt[i]
		win.addstr(i+10, 1, line)
	dirt = []
	hasChanges = False

keymappings = {
		'KEY_DOWN' : movedown,
		'KEY_UP': moveup,
		'KEY_LEFT' : moveleft,
		'KEY_RIGHT' : moveright,
		'q' : quit,
		'g' : generateDirt
		}



if __name__ == '__main__':
	wrapper(main)
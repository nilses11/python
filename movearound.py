from curses import wrapper
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
import pdb

y = 9
x = 11
loop = True
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
	
	while loop:
		key = win.getkey()
		win.addch(y, x, ' ')
		if key in keymappings:
			keymappings[key]()
		win.move(10, 0)
		for line in dirt:
			win.addstr(line)
			#break
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
	#pdb.set_trace()
	for yes in range(maxyx[0]-15):
		line = ''
		for xes in range(maxyx[1]):
			line+='#'
		dirt.append(line)
	#pdb.set_trace()

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
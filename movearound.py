from curses import wrapper, error
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
import pdb

state = {
	'player' : [9, 11],
	'loop' : True,
	#dirt : []
}
def main(win):
	global state
	win.box()
	state['maxyx'] = win.getmaxyx()
	state['win'] = win
	try:
		win.curs_set(0)
	except:
		pass
	#Set start position
	y, x = state['player']
	#win.addch(y, x, '&')
	win.move(y, x)
	
	while state['loop']:
		key = win.getkey()
		if key in keymappings:
			keymappings[key](state)

def debug(state):
	pdb.set_trace()

def quit(state):
	state['loop'] = False

def moveup(state):
	if (state['player'][0]) > 1:
		clearyx(state)
		state['player'][0]-=1

def moveleft(state):
	if (state['player'][1]) > 1:
		clearyx(state)
		state['player'][1]-=1

def moveright(state):
	if (state['player'][1]) < state['maxyx'][1]-1:
		clearyx(state)
		state['player'][1]+=1

def movedown(state):
	if (state['player'][0]) < state['maxyx'][0]-1:
		clearyx(state)
		state['player'][0]+=1
		

def drawChanges(state):
	y, x = state['player']
	state['win'].addch(y, x, '0')
	state['win'].move(y, x)
	state['win'].redrawwin()

def clearyx(state):
	y, x = state['player']
	state['win'].addch(y, x, ' ')
	state['win'].move(y, x)

def generateDirt(state):
	maxy, maxx = state['maxyx']
	for y in range(1, maxy-1):
		for x in range(1, maxx-1):
			try:
				state['win'].addch(y,x, ord('a'))
			except error as e:
				pass
				pdb.set_trace()


keymappings = {
		'KEY_DOWN' : movedown,
		'KEY_UP': moveup,
		'KEY_LEFT' : moveleft,
		'KEY_RIGHT' : moveright,
		'q' : quit,
		'g' : generateDirt,
		'a' : drawChanges,
		's' : clearyx,
		'd' : debug
		}

if __name__ == '__main__':
	wrapper(main)
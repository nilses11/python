from curses import wrapper, error, A_STANDOUT, A_CHARTEXT, A_UNDERLINE, A_REVERSE, A_BLINK, A_DIM, A_INVIS, A_ALTCHARSET
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from random import randint
import pdb

state = {
	'player' : [0, 10],
	'next' : [0, 10],
	'loop' : True,
	'gems' : 0
}
def main(win):
	global state
	state['maxyx'] = win.getmaxyx()
	state['win'] = win
	try:
		win.curs_set(0)
	except:
		pass
	#Set start position
	y, x = state['player']
	generateDirt(state)
	
	while state['loop']:
		key = win.getkey()
		if key in keymappings:
			keymappings[key](state)

def debug(state):
	pdb.set_trace()

def quit(state):
	state['loop'] = False

def moveup(state):
	state['next'][0]-=1
	move(state)

def moveleft(state):
	state['next'][1]-=1
	move(state)

def moveright(state):
	state['next'][1]+=1
	move(state)

def movedown(state):
	state['next'][0]+=1
	move(state)

def activate(state):
	y, x = state['player']
	state['win'].addch(y, x, 'a')
	state['win'].move(y, x)
	state['win'].redrawwin()

def redraw(state):
	y, x = state['player']
	state['win'].addch(y, x, '&')
	state['win'].move(y, x)

def generateDirt(state):
	#all except 1st and last line
	maxy, maxx = state['maxyx']
	for y in range(1, maxy-1):
		for x in range(0, maxx):
			try:
				if y == 69 and x == 79:
					continue
				state['win'].addch(y,x, ' ', A_STANDOUT)
			except error as e:
				pass
				pdb.set_trace()
	redraw(state)

def printStatus(state, msg="Testmessage"):
	maxy = state['maxyx'][0]
	state['win'].addstr(maxy-1, 0, msg)
	#state['win'].move(y, x)

def move(state):
	if (isBlocked(state)):
		#Player should not be allowed to move here
		state['next'][0] = state['player'][0]
		state['next'][1] = state['player'][1]
	else:
		#Move player!
		if isDirt(state):
			bigMoney(state)
		state['win'].addch(state['player'][0], state['player'][1], ' ')
		state['player'][0] = state['next'][0]
		state['player'][1] = state['next'][1]
		redraw(state)

def bigMoney(state):
	inch = state['win'].inch(state['next'][0], state['next'][1])
	#char = inch & A_CHARTEXT
	isStandout = bool(inch & A_STANDOUT)
	#if (isStandout):
	obj = treasures.keys()[randint(0, len(treasures)-1)]
	#pdb.set_trace()
	if obj in state:
		state[obj]+=1;
	else:
		state['win'].addch(state['next'][0], state['next'][1], 'D', A_STANDOUT)
		state['next'][0] = state['player'][0]
		state['next'][1] = state['player'][1]

def isBlocked(state):
	inch = state['win'].inch(state['next'][0], state['next'][1])
	char = inch & A_CHARTEXT
	isStandout = bool(inch & A_STANDOUT)
	isD = bool(char == 'D')
	isInvis = bool(inch & A_INVIS)
	pdb.set_trace()
	return isInvis or (isD and isStandout) or (state['next'][0] == 69 and state['next'][1] == 79)

def isDirt(state):
	inch = state['win'].inch(state['next'][0], state['next'][1])
	char = inch & A_CHARTEXT
	isStandout = bool(inch & A_STANDOUT)
	isD = bool(char == 'D')
	isInvis = bool(inch & A_INVIS)
	#pdb.set_trace()
	return ((not isD) and isStandout)

"""
debug og redraw brukes ikke
"""
keymappings = {
		'KEY_DOWN' : movedown,
		'KEY_UP': moveup,
		'KEY_LEFT' : moveleft,
		'KEY_RIGHT' : moveright,
		'q' : quit,
		'g' : generateDirt,
		'a' : activate,
		'r' : redraw,
		'd' : debug,
		'b' : bigMoney,
		'p' : printStatus
		}

treasures = {
		'rock' : 0.1,
		'gems' : 0.1
		}

if __name__ == '__main__':
	wrapper(main)


"""
TODO:
legg til bunnlinje som tilbakemelding tekst -> fjerne hack (nederst hyre hjrne...)

MINERVGA?
*grave i moerket
*Items for aa 'se mer'
*skjermbildet selv er fasit, ingen bakomliggende array for 'isUtforsket'?

state['win'].inch(y,x) in ['#', '.']
	#c = a & A_CHARTEXT
	d = a & A_STANDOUT
	#e = a & A_UNDERLINE
	#f = a & A_REVERSE
	#g = a & A_BLINK
	h = a & A_DIM
	#i = a & A_INVIS
	#j = a & A_ALTCHARSET
 
 dic.values()[index]
"""


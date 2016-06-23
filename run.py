import ms
import pdb

loop = 0

ms.printneighbors(ms.board)
print 'Commands:'
print '    o - open'
print '    f - flag'
print '    u - unflag'
print '    s - open all nearby fields that are not flagged'
print '    TODO'
print 'Example:'
print '    "o 0 1"'
print 'opens box at column 0, row 1'


while loop != -1:
	try:
		c,x,y = raw_input().split(' ')
		if c == 'o':
			loop = ms.explore(int(y),int(x))
		elif c == 'f':
			ms.flag(int(y),int(x))
		elif c == 'u':
			ms.unflag(int(y),int(x))
		elif c == 's':
			loop = ms.search(int(y),int(x))
		else:
			print 'Unknown command:',c
		ms.printneighbors(ms.board)
		if ms.checkIsFinished():
			print 'You won!'
			loop = -1
	except ValueError:
		print 'Invalid value'

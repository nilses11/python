from random import randint
board = []
explored = []
flagged = []
boardsize = 20
numbombs = 40

#Setup blank boards for explored and flagged
for p in range(boardsize):
	explored.append([False for i in range(boardsize)])
	flagged.append([False for i in range(boardsize)])

def createBoardWithExactNumbombs():
	b2 = [[" " for x in range(boardsize)] for y in range(boardsize)]
	for i in range(numbombs):
		y = randint(0, boardsize-1)
		x = randint(0, boardsize-1)
		b2[x][y] = '*'
	for i in b2:
		board.append("".join(i))
	return board

def printneighbors(board):
	newboard = []
	for line in range(boardsize):
		newline = ""
		for char in range(boardsize):
			newline+=str(neighbors(board, line, char))
		newboard.append(newline)
	printSolution(newboard)
	return board


def neighbors(board, x, y):
	count = 0
	if x > 0:
		if board[x-1][y]=="*": count+=1
		if y > 0:
			if board[x-1][y-1]=="*": count+=1
		if y < boardsize-1:
			if board[x-1][y+1]=="*": count+=1
	if x < boardsize-1:
		if board[x+1][y]=="*": count+=1
		if y > 0:
			if board[x+1][y-1]=="*": count+=1
		if y < boardsize-1:
			if board[x+1][y+1]=="*": count+=1
	if y > 0:
		if board[x][y-1]=="*": count+=1
	if y < boardsize-1:
		if board[x][y+1]=="*": count+=1
	if board[x][y]=="*":
		return "*"
	return count


def printSolution(board):
	print '  01234567890123456789'
	print ''
	for i in range(boardsize):
		print str(i%10), getVal(board[i], explored[i], flagged[i])

def getVal(line, linexp, fl):
	s = ""
	for c in range(boardsize):
		if linexp[c]:
			s+=line[c]
		elif fl[c]:
			s+="\033[0;31mf\033[0m"
		else:
			s+=" "
	return s


def explore(x, y):
	if checkBounds(x,y) == -1:
		return -1
	if flagged[x][y]:
		return 0
	explored[x][y] = True
	if board[x][y] == '*':
		return -1
	elif neighbors(board, x, y) == 0:
		if x > 0 and not explored[x-1][y]:
			explore(x-1,y)
		if x < boardsize-1 and not explored[x+1][y]:
			explore(x+1,y)
		if y > 0 and not explored[x][y-1]:
			explore(x,y-1)
		if y < boardsize-1 and not explored[x][y+1]:
			explore(x,y+1)


def flag(x,y):
	if checkBounds(x,y) == -1:
		return -1
	if explored[x][y]:
		return 0
	flagged[x][y] = True

def unflag(x,y):
	if checkBounds(x,y) == -1:
		return -1
	if explored[x][y]:
		return 0
	flagged[x][y] = False


def checkBounds(x,y):
	if x < 0:
		return -1
	if y < 0:
		return -1
	if x > boardsize-1:
		return -1
	if y > boardsize-1:
		return -1

board = createBoardWithExactNumbombs()

#Assert that the board is a square
assert len(board) == len(board[0])

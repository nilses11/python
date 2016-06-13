from random import randint
board = []
explored = []
boardsize = 20
numbombs = 40

for p in range(boardsize):
	explored.append([False for i in range(boardsize)])

def createRandomBoard():
	for i in range(boardsize):
		s = ""
		for o in range(boardsize):
			if randint(0,numbombs) < 1:
				s+="*"
			else:
				s+=" "
		board.append(s)


def createBoardWithExactNumbombs():
	b2 = [[" " for x in range(boardsize)] for y in 
range(boardsize)]
	for i in range(numbombs):
		y = randint(0, boardsize-1)
		x = randint(0, boardsize-1)
		b2[x][y] = '*'
	for i in b2:
		board.append("".join(i))
	return board
	

#createRandomBoard()
board = createBoardWithExactNumbombs()
assert len(board) == len(board[0])

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
	print '  0123456789'
	print ''
	for i in range(boardsize):
		print str(i%10), getVal(board[i], explored[i])

def getVal(line, linexp):
	s = ""
	for c in range(boardsize):
		if linexp[c]:
			s+=line[c]
		else:
			s+=" "
	return s

def explore(x, y):
	if x < 0:
		return -1
	if y < 0:
		return -1
	if x > boardsize-1:
		return -1
	if y > boardsize-1:
		return -1

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

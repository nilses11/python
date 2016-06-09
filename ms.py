board = []

board.append("*        *")
board.append("          ")
board.append("          ")
board.append("          ")
board.append("   *   *  ")
board.append("     ***  ")
board.append("          ")
board.append("          ")
board.append("  *       ")
board.append("*        *")


def printneighbors(board):
	newboard = []
	for line in range(len(board)):
		newline = ""
		for char in range(len(board[line])):
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
		if y < len(board)-1:
			if board[x-1][y+1]=="*": count+=1
	if x < len(board)-1:
		if board[x+1][y]=="*": count+=1
		if y > 0:
			if board[x+1][y-1]=="*": count+=1
		if y < len(board)-1:
			if board[x+1][y+1]=="*": count+=1
	if y > 0:
		if board[x][y-1]=="*": count+=1
	if y < len(board)-1:
		if board[x][y+1]=="*": count+=1

	if board[x][y]=="*":
		return "*"

	return count

def printSolution(board):
	print '  ABCDEFGHIJ'
	for i in range(len(board)):
		print str(i), board[i]

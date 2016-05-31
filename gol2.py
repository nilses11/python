import os
import time

os.system('clear')


def makeboard():
	board = []
	board.append("                    ")
	board.append("                    ")
	board.append("   *                ")
	board.append("    *               ")
	board.append("  ***               ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	board.append("                    ")
	return board

def printboard(board):
	for line in board:
		print line
	return board


def next(board):
	newboard = []
	for line in range(len(board)):
		newline = ""
		for char in range(len(board[line])):
			if neighbors(board, line, char) < 2:
				newline+=" "
			elif neighbors(board, line, char) == 2:
				newline+=board[line][char]
			elif neighbors(board, line, char) == 3:
				newline+="*"
			elif neighbors(board, line, char) > 3:
				newline+=" "
			else:
				err = neighbors(board, line, char)
				raise ValueError(err)
		newboard.append(newline)
	return newboard

def printneighbors(board):
	newboard = []
	for line in range(len(board)):
		newline = ""
		for char in range(len(board[line])):
			newline+=str(neighbors(board, line, char))
		newboard.append(newline)
	printboard(newboard)
	return board
	

def neighbors(board, x, y):
	count = 0
	if (x > 1) & (x < len(board)-1) & (y > 1) & (y < 
len(board[0])-1):
		if board[x-1][y]=="*": count+=1
		if board[x+1][y]=="*": count+=1
		if board[x-1][y+1]=="*": count+=1
		if board[x-1][y-1]=="*": count+=1
		if board[x][y+1]=="*": count+=1
		if board[x][y-1]=="*": count+=1
		if board[x+1][y+1]=="*": count+=1
		if board[x+1][y-1]=="*": count+=1
	return count


s = makeboard()

#while s != "q":
	#print s
	#s = input()


for aaa in range(25):
	os.system('clear')
	s = printboard(s)
	s = next(s)
	time.sleep(0.1)

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
        print(line)
    return board


def next_step(board):
    newboard = []
    for linenumber, line in enumerate(board):
        newline = ""
        for charnumber, _ in enumerate(line):
            if neighbors(board, linenumber, charnumber) < 2:
                newline+=" "
            elif neighbors(board, linenumber, charnumber) == 2:
                newline+=board[linenumber][charnumber]
            elif neighbors(board, linenumber, charnumber) == 3:
                newline+="*"
            elif neighbors(board, linenumber, charnumber) > 3:
                newline+=" "
            else:
                err = neighbors(board, linenumber, charnumber)
                raise ValueError(err)
        newboard.append(newline)
    return newboard

def printneighbors(board):
    newboard = []
    for linenumber, line in enumerate(board):
        newline = ""
        for charnumber, _ in enumerate(line):
            newline+=str(neighbors(board, linenumber, charnumber))
        newboard.append(newline)
    return board

def neighbors(board, x, y):
    count = 0
    if (x > 1) & (x < len(board)-1) & (y > 1) & (y < len(board[0])-1):
        if board[x-1][y]=="*":
            count+=1
        if board[x+1][y]=="*":
            count+=1
        if board[x-1][y+1]=="*":
            count+=1
        if board[x-1][y-1]=="*":
            count+=1
        if board[x][y+1]=="*":
            count+=1
        if board[x][y-1]=="*":
            count+=1
        if board[x+1][y+1]=="*":
            count+=1
        if board[x+1][y-1]=="*":
            count+=1
    return count


s = makeboard()

while s != "q":
    s = printboard(s)
    tmp = input()
    if tmp == "q":
        s = tmp
    else:
        s = next_step(s)
        os.system('clear')


""" for aaa in range(25):
    os.system('clear')
    s = printboard(s)
    s = next_step(s)
    time.sleep(0.1)
 """
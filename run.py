import ms


loop = 0


ms.printneighbors(ms.board)

while loop != -1:
	x,y = input()
	loop = ms.explore(y,x)
	ms.printneighbors(ms.board)


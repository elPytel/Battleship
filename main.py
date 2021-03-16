# By Pytel
'''
Hra lode v terminalu s jednoduchym AI.
'''

import copy
import Ships
import AI

# new game with new players
game = Ships.Game()
game.MakeBoards()
game.MakeShips()
game.SetPlayer(1, AI.Player())
game.SetPlayer(2, AI.Player())

# inicializace
while True != False:
	game.player1.Init(game.board.p1, copy.deepcopy( game.Ships() ) )
	if game.ValidBoardPlayer(1):
		break
	game.ResetBoardPlayer(1)

while True != False:
	game.player2.Init(game.board.p2, copy.deepcopy( game.Ships() ))
	if game.ValidBoardPlayer(2):
		break
	game.ResetBoardPlayer(2)
	
game.Print()
exit()

# hra
if not game.PlayersSet():
	print("ERROR: players arent set!")

while True != False:
	# hrac 1
	hit = True
	while hit == True:
		# mel by posilat deep copy kvuli pravum
		move = game.player1.Play( copy.deepcopy(game.board.p1) )
		if game.ValidMove(1, move):
			hit = not game.IsMiss(1, move)
			game.ExecuteMove(1, move)
		else:
			print("Invalid move!")
			break
		
		# zabil ho?
		if not game.Alive(2):
			break
		else:
			game.board.Print()
	
	# zabil ho?
	if not game.Alive(2):
		break
	else:
		game.board.Print()
	
	# hrac 2
	hit = true
	while hit == True:
		move = game.player2.Play( copy.deepcopy(game.board) )
		if game.ValidMove(2, move):
			game.ExecuteMove(2, move)
		else:
			print("Invalid move!")
			break
			
		# zabil ho?
		if not game.Alive(1):
			break
		else:
			game.board.Print()
	
	# zabil ho?
	if not game.Alive(1):
		break
	else:
		game.board.Print()


print(" ---Final Bord--- ") 
game.Print()
'''

'''
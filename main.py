# By Pytel
'''
Hra lode v terminalu s jednoduchym AI.
'''

import copy
import Game
import Boards
import AI
import AI_old

DEBUG = True

# new game with new players
game = Game.Game()
game.MakeBoards()
game.MakeShips()
game.SetPlayer(1, AI.Player())
game.SetPlayer(2, AI_old.Player())

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
	

# hra
if not game.PlayersSet():
	print("ERROR: players arent set!")

while True != False:
	# hrac 1
	hit = True
	state = []
	while hit == True:
		state = None		# 
		move = game.player1.Play(copy.deepcopy(game.board.p1),  state)
		if game.ValidMove(1, move):
			hit = game.IsHit(1, move)
			if hit:
				state = ["hit"]
				game.LowerLives(2)
				print("It is a hit. Repeating turn!")
			game.ExecuteMove(1, move)
		else:
			print("Invalid move!")
			break
		# zabil ho?
		if not game.Alive(2):
			break
	
	# zabil ho?	
	if not game.Alive(2):
		break
	
	# hrac 2
	hit = True
	state = []
	while hit == True:
		move = game.player2.Play(copy.deepcopy(game.board.p2), state)
		if game.ValidMove(2, move):
			hit = game.IsHit(2, move)
			if hit:
				game.LowerLives(1)
				print("It is a hit. Repeating turn!")
			game.ExecuteMove(2, move)
		else:
			print("Invalid move!")
			break
		# zabil ho?
		if not game.Alive(1):
			break
	
	# zabil ho?
	if not game.Alive(1):
		break
	else:
		game.board.Print()


print(" ---Final Bord--- ") 
game.Print()
game.PrintLives()
'''

'''
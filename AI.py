# By Pytel

import random
import Boards

DEBUG = True
BOARD_X_SIZE = 10
BOARD_Y_SIZE = 10

class Player:
	def __init__(self):
		self.board = Boards.Board()
		self.my_board = None
		self.enemy_board = None
		self.ships = []
	
	def Init(self, boards, ships):
		self.my_board = boards[0]
		self.enemy_board = boards[1]
		self.ships = ships
		vectors = [ [1,0], [0,1], [-1,0], [0,-1]]
		
		# place all ships
		while len(self.ships) > 0:
			direction = random.choice(vectors)
			ship = random.choice(self.ships)
			
			if DEBUG:
				print(direction)
				ship.Print()
			
			# Odstran tuto loď z vyctu
			# TODO
			if ship.Quantity() == 0:
				if DEBUG:
					print("No ship of this type")
				self.ships.remove(ship)
				continue
				
			else:
				valid = False
				while valid == False:
					position = [	
						random.randrange(-1, BOARD_Y_SIZE), 
						random.randrange(-1, BOARD_X_SIZE)]
						
					# pasuje tam?
					valid = ship.DoesShipFitsToBoard(self.my_board, position, direction)	
					if DEBUG:
						print("Position:", position)
						print("Validity:", valid)
							
					# umisteni
					if valid:
						ship.PlaceShipToBoard(self.my_board, position, direction)
						Boards.Board.PrintBoard(self.my_board)
						ship.LowerQuantity()
			
		
	def Unknouwn(self):
		places = []
		for y in range(Boards.Board.BoardSize('y')):
			for x in range(Boards.Board.BoardSize('x')):
				if self.enemy_board[y][x] == None:
					places.append([y,x])
		return places
	
	def Move(self):
		coords = self.Unknouwn()
		'''
		# coord = [y,x]
		coord = [	
			random.randrange(0, BOARD_Y_SIZE), 
			random.randrange(0, BOARD_X_SIZE)]
		'''
		coord = random.choice(coords)
		return coord
	
	def Play(self, boards):
		self.my_board = boards[0]
		self.enemy_board = boards[1]
		
		shot = self.Move()
		return shot
		

# test
'''
game = Ships.Game()
game.MakeBoards()
game.MakeShips()
game.SetPlayer(1, Player())
while True != False:
	game.player1.Init(game.board.p1, game.Ships())
	game.Print()
	if game.ValidBoardPlayer(1):
		break
	game.ResetBoardPlayer(1)

#game.Print()
'''
	
'''

'''
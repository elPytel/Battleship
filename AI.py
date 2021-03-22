# By Pytel

import random
import Boards

DEBUG = True

class Player:
	def __init__(self):
		self.board = Boards.Board()
		self.my_board = None
		self.enemy_board = None
		self.my_ships = []
		# TODO
		self.shots = []			#[ [[y],[x],[True/False]], ...]
		self.board = []
		self.enemy_ships = []
	
	def Init(self, boards, ships):
		self.my_board = boards[0]
		self.enemy_board = boards[1]
		self.my_ships = ships
		vectors = [ [1,0], [0,1], [-1,0], [0,-1]]
		
		# place all ships
		while len(self.my_ships) > 0:
			direction = random.choice(vectors)
			ship = random.choice(self.my_ships)
			
			if DEBUG:
				print(direction)
				ship.Print()
			
			# Odstran tuto loď z vyctu
			# TODO
			if ship.Quantity() == 0:
				if DEBUG:
					print("No ship of this type")
				self.my_ships.remove(ship)
				continue
				
			else:
				valid = False
				while valid == False:
					position = [	
						random.randrange(-1, Boards.Board.BoardSize('y')), 
						random.randrange(-1, Boards.Board.BoardSize('x'))]
						
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
		coord = random.choice(coords)
		return coord
	
	def Play(self, boards, state):
		# vyhodnoceni predchoziho tahu
		if len(self.shots) != 0:
			if state == "hit":
				self.shots[-1][2] = True 
			else:
				self.shots[-1][2] = False
		
		self.my_board = boards[0]
		self.enemy_board = boards[1]
		
		shot = self.Move()
		self.shots.append([[shot[0]],[shot[1]],[None]])
		return shot
		

# test
if __name__ == '__main__':
	import Game
	game = Game.Game()
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
		# coord = [y,x]
		coord = [	
			random.randrange(0, BOARD_Y_SIZE), 
			random.randrange(0, BOARD_X_SIZE)]
END
'''
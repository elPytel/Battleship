# By Pytel

import Boards
import Ships

class Game:
	def __init__(self):
		self.board = Boards.Board()
		self.ships = []
		self.player1 = None
		self.p1_lives = 0
		self.player2 = None
		self.p2_lives = 0
	
	def ResetBoardPlayer(self, number):
		self.board.MakeBoardPlayer(number)
		
	def MakeBoards(self):
		self.board.MakeBoards()
	
	def SetPlayer(self, number, player):
		if number == 1:
			self.player1 = player
		elif number ==  2:
			self.player2 = player
		else:
			return False
		return True
		
	def PlayersSet(self):
		if self.player1 == None or self.player2 == None:
			return False
		return True
		
	def MakeShips(self):
		ship_types = Ships.Ship()
		for ship_type in ship_types.ShipTypes():
			ship = Ships.Ship()
			ship.MakeShipeType(ship_type, len(ship_types.ShipTypes())-ship_type +1 )
			self.ships.append(ship)
			if 0 and DEBUG:
				print("Making ship type:", ship_type)
				ship.Print()
		
	def Ships(self):
		return self.ships
		
	def PlayerLives(self, player):
		if player == 1:
			return Boards.Board.PlayerLives(self.board.p1[0])
		elif player == 2:
			return Boards.Board.PlayerLives(self.board.p2[0])
		else:
			return False
		
	def LowerLives(self, player):
		if player == 1:
			self.p1_lives = self.p1_lives -1
			return True
		elif player == 2:
			self.p2_lives = self.p2_lives -1
			return True
		else:
			return False
	
	def ValidBoardPlayer(self, player):
		if player == 1:
			self.p1_lives = self.PlayerLives(player)
			return Boards.Board.ValidBoard(self.board.p1)
		elif player == 2:
			self.p2_lives = self.PlayerLives(player)
			return Boards.Board.ValidBoard(self.board.p2)
		else:
			return False
		return True
		
	def Alive(self, player):
		if player == 1:
			return True if self.p1_lives > 0 else False
		elif player == 2:
			return True if self.p2_lives > 0 else False
		
	def IsMiss(self, player, move):
		y = move[0]
		x = move[1]
		if player == 1:
			return Boards.Board.IsFree(self.board.p2[0], y, x)
		elif player == 2:
			return Boards.Board.IsFree(self.board.p1[0], y, x)
			
	def IsHit(self, player, move):
		y = move[0]
		x = move[1]
		if player == 1:
			return Boards.Board.IsHit(self.board.p2[0], y, x)
		elif player == 2:
			return Boards.Board.IsHit(self.board.p1[0], y, x)
		
	def ValidMove(self, player, move):
		y = move[0]
		x = move[1]
		# jsou to validni souradnice?
		if not Boards.Board.ValidCoord(y, x):
			return False
		# hraje tam poprve?
		if player == 1:
			if not Boards.Board.IsFree(self.board.p1[1], y, x):
				return False
		elif player == 2:
			if not Boards.Board.IsFree(self.board.p2[1], y, x):
				return False
		return True
	
	def ExecuteMove(self, player, move):
		y = move[0]
		x = move[1]
		if player == 1:
			my_board = self.board.p1[1]
			enemy_board = self.board.p2[0]
		elif player == 2:
			my_board = self.board.p2[1]
			enemy_board = self.board.p1[0]
		
		if enemy_board[y][x] == 1:
			enemy_board[y][x] = -1
			my_board[y][x] = -1
		else:
			enemy_board[y][x] = 0
			my_board[y][x] = 0
	
	def PrintLives(self):
		print(" Lives:")
		print("Player1:", self.p1_lives)
		print("Player2:", self.p2_lives)
	
	def PrintShips(self):
		for ship in self.ships:
			ship.Print()
	
	def Print(self):
		self.board.Print()

# test
'''
game = Game()
game.MakeBoards()
game.MakeShips()
game.Print()
game.PrintShips()
'''
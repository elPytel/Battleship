# By Pytel

import random

DEBUG = True
BOARD_X_SIZE = 10
BOARD_Y_SIZE = 10

def RotateToRight(vektor):
	y = vektor[0]
	x = vektor[1]
	if y == 1 and x == 0:
		rotated = [0,1]
	elif y == 0 and x == 1:
		rotated = [-1,0]
	elif y == -1 and x == 0:
		rotated = [0,-1]
	elif y == 0 and x == -1:
		rotated = [1,0]
	else:
		rotated = [0,0]
	return rotated

class Ship:
	def __init__(self):
		self.types = [1, 2, 3, 4]
		self.name = None
		self.quantity = 0
		self.shape = None
		
	def MakeShipeType(self, name, quantity):
		self.name = name
		self.quantity = quantity
		
		if name == 1:
			self.shape = [
			[None, 'f', None],
			['f', 'x', 'f'],
			[None, 'f', None],
			]
		elif name == 2:
			self.shape = [
			[None, 'f', 'f', None],
			['f', 'x', 'x', 'f'],
			[None, 'f', 'f', None],
			]
		elif name == 3:
			self.shape = [
			[None, 'f', 'f', 'f', None],
			['f', 'x', 'x', 'x', 'f'],
			[None, 'f', 'f', 'f', None],
			]
		elif name == 4:
			self.shape = [
			[None, 'f', 'f', 'f', 'f', None],
			['f', 'x', 'x', 'x', 'x', 'f'],
			[None, 'f', 'f', 'f', 'f', None],
			]
		else:
			print("ERROR: unknown ship type!")
			return False
		return True
		
	def ShipTypes(self):
		return self.types
	
	def Quantity(self):
		return self.quantity
	
	def LowerQuantity(self):
		if self.quantity <= 0:
			return False
		else:
			self.quantity = self.quantity -1
			return True
		
	def DoesShipFitsToBoard(self, board, position, direction):
		valid = True
		col = 0
		for line in self.shape:
			if not valid:
				break
			else:
				vektor = RotateToRight(direction)	
				y = position[0] + vektor[0]*col
				x = position[1] + vektor[1]*col
				col = col +1
			for box in line:
				y = y + direction[0]
				x = x + direction[1]
				if box == None:
					continue
				if not Board.ValidCoord(y, x):
					if box == 'x':
						valid = False
						break
					if box == 'f':
						continue
				# pozice je validni
				if box == 'f' or box == 'x':
					if 0 and DEBUG:
						print("Y:", y, "X:", x)
					if not Board.IsFree(board, y, x):
						valid = False
						break
		return valid
		
	def PlaceShipToBoard(self, board, position, direction):
		col = 0
		for line in self.shape:
			vektor = RotateToRight(direction)	
			y = position[0] + vektor[0]*col
			x = position[1] + vektor[1]*col
			col = col +1
			for box in line:
				y = y + direction[0]
				x = x + direction[1]
				if box == 'x':
					board[y][x] = 1
		
	def Print(self):
		print("Name:", self.name)
		print("Quantity:", self.quantity)
		for col in self.shape:
			for row in col:
				if row == None:
					print(" ", end='')
				elif row == 'f':
					print(" ", end='')
				elif row == 'x':
					print("x", end='')
				else:
					print("ERROR while printing ship!")
					return False
			print()
		return True

class Board:
	def __init__(self):
		self.board_x_size = BOARD_X_SIZE
		self.board_y_size = BOARD_Y_SIZE
		
		self.board_p1_ships = None
		self.board_p1_enemy = None
		self.p1 = []
		self.p1.append(self.board_p1_ships)
		self.p1.append(self.board_p1_enemy)
		
		self.board_p2_ships = None
		self.board_p2_enemy = None
		self.p2 = []
		self.p2.append(self.board_p2_ships)
		self.p2.append(self.board_p2_enemy)
	
	def MakeBoard(self):
		board = []
		for y in range(BOARD_Y_SIZE):
			row = []
			for x in range(BOARD_X_SIZE):
				row.append(None)
			board.append(row)
		return board
		
	def MakeBoards(self):
		self.board_p1_ships = self.MakeBoard()
		self.board_p1_enemy = self.MakeBoard()
		self.p1[0] = self.board_p1_ships
		self.p1[1] = self.board_p1_enemy
		
		self.board_p2_ships = self.MakeBoard()
		self.board_p2_enemy = self.MakeBoard()
		self.p2[0] = self.board_p2_ships
		self.p2[1] = self.board_p2_enemy
	
	def MakeBoardPlayer(self, number):
		if number == 1:
			self.board_p1_ships = self.MakeBoard()
			self.board_p1_enemy = self.MakeBoard()
		elif number ==  2:
			self.board_p2_ships = self.MakeBoard()
			self.board_p2_enemy = self.MakeBoard()
		else:
			return False
		return True 
		
	#def ValidSquare(self, board, y, x):
		# TODO
	
	def IsFree(board, y, x):
		if 0 and DEBUG:
			print("Y:", y, "X:", x)
			print(board[y][x])
		return True if board[y][x] == None else False
	
	def ValidCoord(y, x):
		if y < 0 or BOARD_Y_SIZE <= y:
			return False
		elif x < 0 or BOARD_X_SIZE <= x:
			return False
		else:
			return True
	
	def ValidBoard(boards):
		ret = True
		my_board = boards[0]
		enemy_board = boards[1]
		# is my board set valid?
		# TODO
		
		# is enemy board clear?
		for row in enemy_board:
			for col in row:
				if col != None:
					ret = False
					if DEBUG:
						print("Enemy board is not clear!")
					break
			if ret == False:
				break
		return ret
		
	def PrintBoard(board):
		print(" ", end='')
		for number in range(BOARD_X_SIZE):
			print("", number+1, end='')
		
		print()	
		print(" " + "-"*(2*BOARD_X_SIZE+1))
		index = 0
		for colum in board:
			letter = chr(ord("A") + index)
			print(letter, end='')
			print("|", end='')
			for row in colum:
				if row == None:
					print(" |", end='')
				elif row == 0:
					print("o|", end='')
				elif row == 1:
					print("s|", end='')
				elif row == -1:
					print("x|", end='')
			print()
			index = index +1
		print(" " + "-"*(2*BOARD_X_SIZE+1))
		print()	
		
	def PrintPlayer(boards):
		my_board = boards[0]
		enemy_board = boards[1]
		print(" ", end='')
		for number in range(BOARD_X_SIZE):
			print("", number+1, end='')
		print("	 ", end='')
		for number in range(BOARD_X_SIZE):
			print("", number+1, end='')
		
		print()	
		print(" " + "-"*(2*BOARD_X_SIZE+1), end='')
		print("	", end='')
		print(" " + "-"*(2*BOARD_X_SIZE+1))
		index = 0
		for y in range(BOARD_Y_SIZE):
			letter = chr(ord("A") + index)
			print(letter, end='')
			print("|", end='')
			for x in range(BOARD_X_SIZE):
				if my_board[y][x] == None:
					print(" |", end='')
				elif my_board[y][x] == 0:
					print("o|", end='')
				elif my_board[y][x] == 1:
					print("s|", end='')
				elif my_board[y][x] == -1:
					print("x|", end='')
			print("	", end='')
			letter = chr(ord("A") + index)
			print(letter, end='')
			print("|", end='')
			for x in range(BOARD_X_SIZE):
				if enemy_board[y][x] == None:
					print(" |", end='')
				elif enemy_board[y][x] == 0:
					print("o|", end='')
				elif enemy_board[y][x] == 1:
					print("s|", end='')
				elif enemy_board[y][x] == -1:
					print("x|", end='')
			print()
			
			index = index +1
		print(" " + "-"*(2*BOARD_X_SIZE+1), end='')
		print("	", end='')
		print(" " + "-"*(2*BOARD_X_SIZE+1))
		print()	
				
	def Print(self):
		Board.PrintPlayer(self.p1)
		Board.PrintPlayer(self.p2)
		'''
		Board.PrintBoard(self.board_p1_ships)
		Board.PrintBoard(self.board_p1_enemy)
		Board.PrintBoard(self.board_p2_ships)
		Board.PrintBoard(self.board_p2_enemy)
		'''

class Game:
	def __init__(self):
		self.board = Board()
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
		ship_types = Ship()
		for ship_type in ship_types.ShipTypes():
			ship = Ship()
			ship.MakeShipeType(ship_type, len(ship_types.ShipTypes())-ship_type +1 )
			self.ships.append(ship)
			if 0 and DEBUG:
				print("Making ship type:", ship_type)
				ship.Print()
		
	def Ships(self):
		return self.ships
	
	def ValidBoardPlayer(self, number):
		if number == 1:
			return Board.ValidBoard(self.board.p1)
		elif number == 2:
			return Board.ValidBoard(self.board.p2)
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
			return Board.IsFree(self.board.p2[0], y, x)
		elif player == 2:
			return Board.IsFree(self.board.p1[0], y, x)
		
	def ValidMove(self, player, move):
		# TODO
		y = move[0]
		x = move[1]
		'''
		if player == 1:
		elif player == 2:
		'''
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
			my_board = -1
		else:
			enemy_board[y][x] = 0
			my_board = 0
	
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

"""
Jak budu reprezentovat lode?
4*1, 3*2, 2*3, 1*4
self.ships = [ 	['x'],
				['x', 'x'],
				['x', 'x', 'x'],
				['x', 'x', 'x', 'x'], ]

[
[None, 'f', None],
['f', 'x', 'f'],
[None, 'f', None],
],

[
[None, 'f', 'f', None],
['f', 'x', 'x', 'f'],
[None, 'f', 'f', None],
],

[
[None, 'f', 'f', 'f', None],
['f', 'x', 'x', 'x', 'f'],
[None, 'f', 'f', 'f', None],
],

[
[None, 'f', 'f', 'f', 'f', None],
['f', 'x', 'x', 'x', 'x', 'f'],
[None, 'f', 'f', 'f', 'f', None],
],
]

[on_true] if [expression] else [on_false] 

print('{0:2d}'.format(number+1), end='')

Ships file END
"""
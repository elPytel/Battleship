# By Pytel

import Ships
import Game

DEBUG = False
BOARD_X_SIZE = 10
BOARD_Y_SIZE = 10

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
		
	def BoardSize(dimension):
		board = Board()
		if dimension == 'y':
			return board.board_y_size
		elif dimension == 'x':
			return board.board_x_size
		return None
		
	#def ValidSquare(self, board, y, x):
		# TODO
	
	def IsFree(board, y, x):
		if 0 and DEBUG:
			print("Y:", y, "X:", x)
			print(board[y][x])
		return True if board[y][x] == None else False
		
	def IsHit(board, y, x):
		if 0 and DEBUG:
			print("Y:", y, "X:", x)
			print(board[y][x])
		return True if board[y][x] == 1 else False
	
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
		positions = []
		ships = []
		ship_types = []
		'''
		for x in range(Board.BoardSize('x') ):
			for y in range(Board.BoardSize('y') ):
				if my_board[y][x] == 1 and my_board[y][x] not in ships:
					positions = Ships.Ship.IsValidShip(my_board, y, x)
					# [[True/False], [positions...]]
					if positions[0] == True:
						ship_types.append(positions[1])
						ships.append(positions[2])
					else:
						ret = False
						break
			if ret == False:
				break
			
		if ret == True and not Game.Game.IsValidSetOfShips(ship_types):
			ret = False
		'''
		if ret == True:
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
	
	def PlayerLives(board):
		lives = 0
		
		for line in board:
			for box in line:
				if box == 1:
					lives = lives +1
		
		return lives
		
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

"""
End
"""
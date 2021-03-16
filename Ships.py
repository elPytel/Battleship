# By Pytel

import random
import Boards

DEBUG = True

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
				if not Boards.Board.ValidCoord(y, x):
					if box == 'x':
						valid = False
						break
					if box == 'f':
						continue
				# pozice je validni
				if box == 'f' or box == 'x':
					if 0 and DEBUG:
						print("Y:", y, "X:", x)
					if not Boards.Board.IsFree(board, y, x):
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
		
	# dostane pozici a prohleda okoli aby zjistil zda tam lezi validni lod.
	def IsValidShip(myboard, y, x):
		valid = True
		if mybord[y][x] != 1:
			valid = False
			return ret
		
		positions = []
		ship_type = -1
		
		#TODO
		
		
		ret.append(valid)
		ret.append(ship_type)
		ret.append(positions)
		return ret
		
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

"""

Ships file END
"""
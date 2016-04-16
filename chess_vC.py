#!/usr/local/bin/python3

# Code by Eric Fossas

# Download colorama, cd into the colorama folder and run: python3 setup.py install

import colorama
import sys
from colorama import Fore, Back, Style

# Black Pieces: Back.BLACK + Fore.WHITE + 
# White Pieces: Back.WHITE + Fore.RESET + 
# Board: Style.RESET_ALL



# id = P pawn, R rook, N knight, B bishop, Q queen, K king
# color = False black, True white
# state = False dead, True alive
class Piece:
	
	_id = ''
	_color = False 
	_state = False
	_move = None
	
	def __init__(self,id,color,move):
		self.setID(id)
		self.setColor(color)
		self.setState(1)
		self.move = move
		
	def setID(self,id):
		self._id = id
		
	def getID(self):
		return self._id
		
	def setColor(self,color):
		self._color = color
		
	def getColor(self):
		return self._color
		
	def setState(self,state):
		self._state = state
		
	def getState(self):
		return self._state
	
	# this will be needed for upgrading pawn, need to change id as well...
	def setMove(self,move):
		self.move = move
	
	def move(self):
		pass
		
	# this is for debugging only!!
	def printPiece(self):
		if(self._color):
			c = 'white'
		else:
			c = 'black'
		if(self._state):
			s = 'alive'
		else:
			s = 'dead'
		print("id: " + self._id + " | color: " + c + " | state: " + s)

# all should inherit from Piece class
# uses movements to add on to origin as possible moves. doesn't check legality of move, just lists possibilities
def King():
	_id = K
	possibleMoves = [ (-1, -1), (-1, 0), (-1, 1) (0, -1), (1, -1), (1, 0), (0, 1), (1, 1) ]

def Queen():
	_id = Q
	possibleMoves = [ (-1, -1), (-1, 0), (-1, 1) (0, -1), (1, -1), (1, 0), (0, 1), (1, 1) ]
	repeatable = True

def Bishop():
	_id = B
	possibleMoves = [ (-1, -1), (-1, 1), (1, -1), (1, 1) ]
	repeatable = True

def Knight():
	_id = N
	possibleMoves = [ (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1) ]

def Rook():
	_id = R
	possibleMoves = [ (1, 0), (-1, 0), (0, 1), (0, -1) ] 
	repeatable = True

#will need to check if movement will take it onto a piece, can't capture like other pieces
#check in legalmove class
def Pawn(isFirstMove, location):
	_id = P
	possibleAttackR = location + (1, 1)
	possibleAttackL = locaion + (-1, 1)
	if isFirstMove = True:
		if Board.isOccupied(possibleAttackR):
			possibleMoves = [ (0, 2), (0, 1), (1, 1) ]
		else if Board.isOccupied(possibleAttackL):
			possibleMoves = [ (0, 2), (0, 1), (-1, 1) ]
		else:
			possibleMoves = [ (0, 2), (0, 1) ]
	else:
		possibleMoves = [(0, 1)]

class Board:
	 
	 # board will store piece positions
	 # death will store dead pieces
	_board = [[' ' for x in range(8)] for x in range(8)]
	_death = []
	
	def __init__(self):
		self._board[0][0] = Piece('R',False,Rook)
		self._board[0][1] = Piece('N',False,Knight)
		self._board[0][2] = Piece('B',False,Bishop)
		self._board[0][3] = Piece('Q',False,Queen)
		self._board[0][4] = Piece('K',False,King)
		self._board[0][5] = Piece('B',False,Bishop)
		self._board[0][6] = Piece('N',False,Knight)
		self._board[0][7] = Piece('R',False,Rook)
		for i in range(8):
			self._board[1][i] = Piece('P',False,Pawn)
		for i in range(8):
			self._board[6][i] = Piece('P',True,Pawn)
		self._board[7][0] = Piece('R',True,Rook)
		self._board[7][1] = Piece('N',True,Knight)
		self._board[7][2] = Piece('B',True,Bishop)
		self._board[7][3] = Piece('Q',True,Queen)
		self._board[7][4] = Piece('K',True,King)
		self._board[7][5] = Piece('B',True,Bishop)
		self._board[7][6] = Piece('N',True,Knight)
		self._board[7][7] = Piece('R',True,Rook)
	
	def printPiece(self,piece):
		# string = blank square, object = piece
		if(type(piece) is str):
			print(" " + piece + " ",end="")
		else:
			if(piece.getColor()):
				print(Back.WHITE + Fore.RESET + " " + piece.getID() + " ",end="")
				print(Style.RESET_ALL + "",end="")
			else:
				print(Back.BLACK + Fore.WHITE +  " " + piece.getID() + " ",end="")
				print(Style.RESET_ALL + "",end="")
	
	def printBoard(self):
		xGrid = ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ']
		yGrid = ['1', '2', '3', '4', '5', '6', '7', '8']
		for i in range(1):
			for j in range(8):
				print("| ",end=xGrid[j])
			print("|")
		print("---------------------------------")
		for i in range(8):
			for j in range(8):
				print("|",end="")
				self.printPiece(Board._board[i][j])
			print("|",yGrid[i])
			print("---------------------------------")
			
	def getPiece(self,location):
		pass
	
class Game:
	
	_playerturn = True
	_origin = ''
	_destination = ''
	
	def __init__(self):
		self._playerturn = True
	
	def printPlayerTurn(self):
		if(self._playerturn):
			print(Back.WHITE + Fore.RESET + "Player White ->",end="")
			print(Style.RESET_ALL + "")
		else:
			print(Back.BLACK + Fore.WHITE + "Player Black ->",end="")
			print(Style.RESET_ALL + "")
	
	def switchPlayerTurn(self):
		self._playerturn = not self._playerturn
	
	# converts chess square "c2" into string of number for board array "12" -> [1][2] (number switch is due to "col,row" -> [row][col])
	def chessToMatrix(self,location):
		result = ''
		if len(location) != 2:
			return False
		else:
			loc = list(location)
			letter = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
			number = {1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7}
			if loc[0] in letter:
				result += str(letter[loc[0]])
			else:
				return False
			if int(loc[1]) in number:
				result += str(number[int(loc[1])])
			else:
				return False
			return result

	def askSquareOrigin(self):
		self._origin = input('Origin: ')
		
	def askSquareDestination(self):
		self._destination = input('Destination: ')
		
	def getOrigin(self):
		return self._origin

	def getDestination(self):
		return self._destination

	def isLegalMove(_origin, _destination, Piece._id):
		# for B, Q, R, need to check if piece in the way.
		options = {P : pawn, R : rook, B : bishop, N : knight, Q : queen, K : king}
		def pawn():
			if _destination - _origin is in pawn.possibleMoves:
				return True
			else:
				return False
		def rook():
			if _destination - _origin is in rook.possibleMoves:
				#repeatable
				return True
			else:
				return False
		def bishop():
			if _destination - origin is in bishop.possibleMoves:
				#repeatable
				return True
			else:
				return False
		def knight(): 
			if _destination - _origin is in knight.possibleMoves:
				return True
			else:
				return False
		def queen():
			if _destination - _origin is in queen.possibleMoves:
				#repeatable
				return True
			else:
				return False
		def king():
			if _destination - _origin is in king.possibleMoves:
				return True
			else: 
				return False

		options[Piece._id]()
			
# This is the actual program code
def main():
	# start up procedure
	chess = Board()
	game = Game()
	
	battle = True
	
	# game logic goes here
	while(battle):
		# player turn
		game.printPlayerTurn()
		game.askSquareOrigin()
		game.askSquareDestination()
		#game.chessToMatrix(game.getOrigin())
		
		# result of turn
		game.switchPlayerTurn()
		chess.printBoard()

# The program executes here
if __name__ == "__main__":
    main()

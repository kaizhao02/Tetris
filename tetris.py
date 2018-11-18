import collections
import sys
import random

class Board:

	def __init__(self, width = 8, height = 20):
		self.width = width
		self.height = height
		self.board = [['.'] * width for _ in range(height)]


	def check_tetris(self):
		for col in range(self.width):
			if board[self.height - 1][col] != "@":
				return 

		self.clear_bottom()

	def clear_bottom(self):
		for i in range(self.height - 1, 0, -1):
			for j in range(self.width - 1, 0, -1):
				board[i][j] = board[i - 1][j]

	def check_bottom(self, piece):
		for point in piece.points:
			x = point[0] + 1
			y = point[1]
			bottom = False
			if x >= self.height or self.board[x][y] != '.':
				self.update_board(piece)
				return True

		return False 

	def update_board(self, piece):
		for point in piece.points:
				self.board[point[0]][point[1]] = '@'

	def print_board(self, piece = None):
		temp = [row[:] for row in self.board]

		for i in range(self.height):
			row = ""
			for j in range(self.width):
				found = False
				if piece:
					for point in piece.points:
						if point[0] == i and point[1] == j:
							row += "@ "
							found = True
				if not found:
					row += temp[i][j] + ' '


				
			print(row)

class Piece:

	def __init__(self, piece_type):
		self.type = piece_type 
		self.init_points()

	def init_points(self):
		if self.type == "I":
			self.points = [(0, 3), (1, 3), (2, 3), (3, 3)]
		elif self.type == "T":
			self.points = [(0, 2), (0, 3), (0, 4), (1, 3)]

	def move_down(self):
		for i in range(len(self.points)):
			self.points[i] = (self.points[i][0] + 1, self.points[i][1])

	def rotate(self):
		for i in range(len(self.points)):
			self.points[i] = (self.points[i][0] + 1, self.points[i][1])


class Game:

	def __init__(self):
		self.board = Board()
		self.possible_pieces = ["I", "T"]
		self.curr_piece = self.get_piece()

	def get_piece(self):
		 piece = random.randint(0, 1)

		 return Piece(self.possible_pieces[piece])

	def press_down(self):
		self.curr_piece.move_down()
		self.board.print_board(self.curr_piece)
		if self.board.check_bottom(self.curr_piece):
			self.curr_piece = Piece("I")


def main(argv):
	b = Board()
	# b.print_board(Piece("I"))
	game = Game()
	game.board.print_board()

	while True:
		move = input()
		if move == "k":
			game.press_down()

if __name__ == "__main__":
	main(sys.argv)
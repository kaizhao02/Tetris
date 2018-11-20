import random
from pieces import Piece

class Board:

	def __init__(self, width = 10, height = 20):
		self.width = width
		self.height = height
		self.board = [['.'] * width for _ in range(height)]
		self.possible_pieces = ["I", "T"]
		self.curr_piece = self.get_random_piece()

	def get_random_piece(self):
		 piece = random.randint(0, 1)

		 return Piece(self.possible_pieces[piece])

	def drop_curr(self):
		while self.can_place_piece(self.curr_piece):
			self.curr_piece.move_down()

		self.curr_piece.move_up()
		self.set_piece(self.curr_piece)
		self.curr_piece = self.get_random_piece()

	def move_curr_down(self):
		self.curr_piece.move_down()
		if not self.can_place_piece(self.curr_piece):
			self.curr_piece.move_up()
			self.set_piece(self.curr_piece)
			self.curr_piece = self.get_random_piece()

	def move_curr_left(self):
		self.curr_piece.move_left()
		if not self.can_place_piece(self.curr_piece):
			self.curr_piece.move_right()

	def move_curr_right(self):
		self.curr_piece.move_right()
		if not self.can_place_piece(self.curr_piece):
			self.curr_piece.move_left()

	def check_tetris(self):
		for col in range(self.width):
			if self.board[self.height - 1][col] != "@":
				return 

		self.clear_bottom()

	def can_place_piece(self, piece):
		for block in piece.blocks:
			if (block.row >= self.height or block.col < 0
										 or block.col >= self.width
										 or self.board[block.row][block.col] != "."): 
				return False

		return True

		# for point in piece.points:
		# 	x = point[0]
		# 	y = point[1]
		# 	bottom = False
		# 	if (x >= self.height or y < 0 
		# 						 or y >= self.width 
		# 						 or self.board[x][y] != '.'):
		# 		return False

		# return True

	def clear_bottom(self):
		for i in range(self.height - 1, 0, -1):
			for j in range(self.width - 1, 0, -1):
				self.board[i][j] = self.board[i - 1][j]

	def check_bottom(self, piece):
		for block in piece.blocks:
			if block.row >= self.height or self.board[x][y] != ".":
				self.set_piece(piece)
				return True

		return False

		# for point in piece.points:
		# 	x = point[0] + 1
		# 	y = point[1]
		# 	bottom = False
		# 	if x >= self.height or self.board[x][y] != '.':
		# 		self.update_board(piece)
		# 		return True

		# return False 

	def set_piece(self, piece):
		for block in piece.blocks:
			self.board[block.row][block.col] = "@"
		# for point in piece.points:
		# 		self.board[point[0]][point[1]] = '@'

	def print_board(self):
		temp = [row[:] for row in self.board]

		for i in range(self.height):
			row = ""
			for j in range(self.width):
				found = False
				
				for block in self.curr_piece.blocks:
					if block.row == i and block.col == j:
						row += "@ "
						found = True
				if not found:
					row += temp[i][j] + " "

				# for point in self.curr_piece.points:
				# 	if point[0] == i and point[1] == j:
				# 		row += "@ "
				# 		found = True
				# if not found:
				# 	row += temp[i][j] + ' '


				
			print(row)
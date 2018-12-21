import random
import pieces

class Board:

	def __init__(self, width = 10, height = 20):
		self.width = width
		self.height = height
		self.board = [['.'] * width for _ in range(height)]
		self.possible_pieces = ["I", "T"]
		self.possible_pieces = {
			0 : pieces.IPiece,
			1 : pieces.OPiece,
			2 : pieces.LPiece,
			3 : pieces.JPiece,
			4 : pieces.SPiece,
			5 : pieces.ZPiece,
			6 : pieces.TPiece
		}
		self.curr_piece = self.get_random_piece()

	def get_random_piece(self):
		piece_num = random.randint(0, 6)		
		piece = self.possible_pieces[piece_num]

		return piece(0, 4)

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

	def rotate_curr_clock(self):
		self.curr_piece.rotate_clockwise()

	def rotate_curr_counter(self):
		self.curr_piece.rotate_counterclockwise()

	def can_place_piece(self, piece):
		for block in piece.blocks:
			if (block.row >= self.height or block.col < 0
										 or block.col >= self.width
										 or self.board[block.row][block.col] != "."): 
				return False

		return True
	
	def set_piece(self, piece):
		for block in piece.blocks:
			self.board[block.row][block.col] = "@"

	def clear_completed_rows(self):
		new_board = [['.'] * self.width for _ in range(self.height)]
		curr_row = self.height - 1

		for row in self.get_uncompleted_rows():
			new_board[curr_row] = list(self.board[row])
			curr_row -= 1

		self.board = new_board

	def get_uncompleted_rows(self):
		uncompleted_rows = []

		for row in range(self.height - 1, -1, -1):
			for col in range(self.width):
				if self.board[row][col] == '.':
					uncompleted_rows.append(row)
					break
			
		return uncompleted_rows



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
				
			print(row)
import collections
import sys
import random
import sched
import time
import os
import msvcrt

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

	def move_up(self):
		for i in range(len(self.points)):
			self.points[i] = (self.points[i][0] - 1, self.points[i][1])

	def move_left(self):
		for i in range(len(self.points)):
			self.points[i] = (self.points[i][0], self.points[i][1] - 1)

	def move_right(self):
		for i in range(len(self.points)):
			self.points[i] = (self.points[i][0], self.points[i][1] + 1)

	def rotate(self):
		for i in range(len(self.points)):
			self.points[i] = (self.points[i][0] + 1, self.points[i][1])

	# def move_to(self, row, col):

class Board:

	def __init__(self, width = 8, height = 20):
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
		self.update(self.curr_piece)
		self.curr_piece = self.get_random_piece()

	def move_curr_down(self):
		self.curr_piece.move_down()
		if not self.can_place_piece(self.curr_piece):
			self.curr_piece.move_up()
			self.update(self.curr_piece)
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
		for point in piece.points:
			x = point[0]
			y = point[1]
			bottom = False
			if (x >= self.height or y < 0 
								 or y >= self.width 
								 or self.board[x][y] != '.'):
				return False

		return True

	def clear_bottom(self):
		for i in range(self.height - 1, 0, -1):
			for j in range(self.width - 1, 0, -1):
				self.board[i][j] = self.board[i - 1][j]

	def check_bottom(self, piece):
		for point in piece.points:
			x = point[0] + 1
			y = point[1]
			bottom = False
			if x >= self.height or self.board[x][y] != '.':
				self.update_board(piece)
				return True

		return False 

	def update(self, piece):
		for point in piece.points:
				self.board[point[0]][point[1]] = '@'

	def print_board(self):
		temp = [row[:] for row in self.board]

		for i in range(self.height):
			row = ""
			for j in range(self.width):
				found = False
				
				for point in self.curr_piece.points:
					if point[0] == i and point[1] == j:
						row += "@ "
						found = True
				if not found:
					row += temp[i][j] + ' '


				
			print(row)

class Game:

	def __init__(self):
		self.board = Board()
		self.tick_scheduler =  sched.scheduler(time.time, time.sleep)

	def clear_screen(self):
		""" Clears the screen
		"""
		if os.name == 'nt':
			os.system('CLS')
		if os.name == 'posix':
			os.system('clear')
		
	def run_ticks(self):
		self.press_down()
		self.tick_scheduler.enter(1, 1, self.run_ticks)


def main(argv):
	b = Board()
	# b.print_board(Piece("I"))
	game = Game()
	game.board.print_board()

	# game.tick_scheduler.enter(1, 1, game.run_ticks)
	# game.tick_scheduler.run()

	while True:
		# s.run()
		move = msvcrt.getch()
		print(move)
		

		if move == b'P':
			game.board.move_curr_down()

		if move == b'K':
			game.board.move_curr_left()

		if move == b'M':
			game.board.move_curr_right()

		if move == b' ':
			game.board.drop_curr()

		if move.lower() == b'\x03':
			break

		# game.clear_screen()
		game.board.check_tetris()
		game.board.print_board()

if __name__ == "__main__":
	main(sys.argv)
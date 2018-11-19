import collections
import sys
import sched
import time
import os
import msvcrt
import datetime

from board import Board

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
		# print(move)
		

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

		game.clear_screen()
		game.board.check_tetris()
		game.board.print_board()

if __name__ == "__main__":
	main(sys.argv)
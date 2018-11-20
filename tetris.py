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
		self.commands = {
			b'P' : self.board.move_curr_down,
			b'K' : self.board.move_curr_left,
			b'M' : self.board.move_curr_right,
			b' ' : self.board.drop_curr,
			b'x' : self.board.rotate_curr_clock,
			b'z' : self.board.rotate_curr_counter,
			b'q' : sys.exit
		}

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
		command = msvcrt.getch()
		# print(move)
		
		move = game.commands.get(command)
		if move:
			move()

		game.clear_screen()
		game.board.check_tetris()
		game.board.print_board()

	# print(".....@.....")
	# print(".....@@...")
	# print("......@...")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print("..........")
	# print(".....a....")
	# print(".....aa...")
	# print("......a...")

if __name__ == "__main__":
	main(sys.argv)
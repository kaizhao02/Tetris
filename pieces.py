
class Block:

	def __init__(self, row, col):
		self.row = row
		self.col = col

class Piece:

	def __init__(self, piece_type):
		self.type = piece_type
		self.blocks = [] 
		self.init_points()

	def init_points(self):
		if self.type == "I":
			self.blocks.extend([Block(0, 3), Block(1, 3), Block(2, 3), Block(3, 3)])
			# self.points = [(0, 3), (1, 3), (2, 3), (3, 3)]
		elif self.type == "T":
			self.blocks.extend([Block(0, 2), Block(0, 3), Block(0, 4), Block(1, 3)])
			# self.points = [(0, 2), (0, 3), (0, 4), (1, 3)]

	def move_down(self):
		for block in self.blocks:
			block.row += 1
		# for i in range(len(self.points)):
		# 	self.points[i] = (self.points[i][0] + 1, self.points[i][1])

	def move_up(self):
		for block in self.blocks:
			block.row -= 1
		# for i in range(len(self.points)):
		# 	self.points[i] = (self.points[i][0] - 1, self.points[i][1])

	def move_left(self):
		for block in self.blocks:
			block.col -= 1
		# for i in range(len(self.points)):
		# 	self.points[i] = (self.points[i][0], self.points[i][1] - 1)

	def move_right(self):
		for block in self.blocks:
			block.col += 1		

		# for i in range(len(self.points)):
		# 	self.points[i] = (self.points[i][0], self.points[i][1] + 1)

	# def rotate(self):
	# 	for i in range(len(self.points)):
	# 		self.points[i] = (self.points[i][0] + 1, self.points[i][1])

	# def move_to(self, row, col):
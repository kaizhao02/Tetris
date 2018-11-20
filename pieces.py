import random

class Block:

	def __init__(self, row, col):
		self.row = row
		self.col = col

class Piece:

	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.blocks = [] 
		self.orientation = 0
		self.update_blocks()

	def update_blocks(self):
		self.blocks = []
		for position in self.relative_block_positions[self.orientation]:
			self.blocks.append(Block(position[0] + self.row, position[1] + self.col))

	def get_random_orientation(self):
		return random.randint(0, self.num_orientations - 1)

	@property
	def num_orientations(self):
		raise NotImplementedError

	@property
	def relative_block_positions(self):
		"""A dict of lists of the positions for each block in the Shape, for each orientation.

		Note: These are *relative* positions as compared to the base position of the current Shape.
		"""
		raise NotImplementedError

	def rotate(self, amount):
		self.orientation = (self.orientation + amount) % self.num_orientations
		self.update_blocks()

	def rotate_clockwise(self):
		self.rotate(1)

	def rotate_counterclockwise(self):
		self.rotate(-1)

	def move_down(self):
		self.row += 1
		for block in self.blocks:
			block.row += 1
		
	def move_up(self):
		self.row -= 1
		for block in self.blocks:
			block.row -= 1
		
	def move_left(self):
		self.col -= 1
		for block in self.blocks:
			block.col -= 1
		
	def move_right(self):
		self.col += 1
		for block in self.blocks:
			block.col += 1		

class IPiece(Piece):
	""" Orientation:  0           90
		======================================
		Shape:      | 0*|   | 0 | 1*| 2 | 3 |
					| 1 |
					| 2 |
					| 3 |
	"""

	@property
	def num_orientations(self):
		return 2

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 0), (1, 0), (2, 0), (3, 0)],
			1: [(0, -1), (0, 0), (0, 1), (0, 2)],
		}

class OPiece(Piece):
	""" Orientation:    0    
		========================
		Shape:      | 0*|| 1 |  
					| 2 || 3 |
					
	"""

	@property
	def num_orientations(self):
		return 1

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 0), (0, 1), (1, 0), (1, 1)],
		}

class LPiece(Piece):
	""" Orientation:  0              90            180           270
		====================================================================
		Shape:      | 0*|             *         | 3 | 2*|         * | 3 |
					| 1 |       | 2 | 1 | 0 |       | 1 |   | 0 | 1 | 2 |
					| 2 | 3 |   | 3 |               | 0 |
	"""

	@property
	def num_orientations(self):
		return 4

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 0), (1, 0), (2, 0), (2, 1)],
			1: [(1, 1), (1, 0), (1, -1), (2, -1)],
			2: [(2, 0), (1, 0), (0, 0), (0, -1)],
			3: [(1, -1), (1, 0), (1, 1), (0, 1)]
		}

class JPiece(Piece):
	""" Orientation:  0              90            180                270
		=========================================================================
		Shape:      | 0*|       | 3 | *             | 2*| 3 |          *   
					| 1 |       | 2 | 1 | 0 |       | 1 |        | 0 | 1 | 2 |
				| 3	| 2 |      	                     | 0 |				 | 3 |	
	"""

	@property
	def num_orientations(self):
		return 4

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 0), (1, 0), (2, 0), (2, -1)],
			1: [(1, 1), (1, 0), (1, -1), (0, -1)],
			2: [(2, 0), (1, 0), (0, 0), (0, 1)],
			3: [(1, -1), (1, 0), (1, 1), (2, 1)]
		}

class JPiece(Piece):
	""" Orientation:  0              90            180                270
		=========================================================================
		Shape:      | 0*|       | 3 | *             | 2*| 3 |          *   
					| 1 |       | 2 | 1 | 0 |       | 1 |        | 0 | 1 | 2 |
				| 3	| 2 |      	                     | 0 |				 | 3 |	
	"""

	@property
	def num_orientations(self):
		return 4

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 0), (1, 0), (2, 0), (2, -1)],
			1: [(1, 1), (1, 0), (1, -1), (0, -1)],
			2: [(2, 0), (1, 0), (0, 0), (0, 1)],
			3: [(1, -1), (1, 0), (1, 1), (2, 1)]
		}

class SPiece(Piece):
	""" Orientation:  0               90
		=====================================
		Shape:      | 0*|         * | 1 | 0 |
					| 1 | 2 |   | 3 | 2 |
						| 3 |
	"""

	@property
	def num_orientations(self):
		return 2

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 0), (1, 0), (1, 1), (2, 1)],
			1: [(0, 2), (0, 1), (1, 1), (1, 0)]
			
		}

class ZPiece(Piece):
	""" Orientation:  0               90
		=====================================
		Shape:        * | 0 |   | 0 | 1*|
					| 2 | 1 |       | 2 | 3 |
					| 3 |
	"""

	@property
	def num_orientations(self):
		return 2

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 1), (1, 1), (1, 0), (2, 0)],
			1: [(0, -1), (0, 0), (1, 0), (1, 1)]
			
		}

class TPiece(Piece):
	""" Orientation:    0           90              180               270
		====================================================================
		Shape:      * | 0 |      * | 1 |          *                 * | 1 |
				  | 1 | 2 | 3 |    | 2 | 0 |    | 1 | 2 | 3 |     | 0 | 2 |
								   | 3 |            | 0 |             | 3 |
	"""

	@property
	def num_orientations(self):
		return 4

	@property
	def relative_block_positions(self):
		return {
			0: [(0, 1), (1, 0), (1, 1), (1, 2)],
			1: [(1, 2), (0, 1), (1, 1), (2, 1)],
			2: [(2, 1), (1, 0), (1, 1), (1, 2)],
			3: [(1, 0), (0, 1), (1, 1), (2, 1)]
		}


	
	# def rotate(self):
	# 	for i in range(len(self.points)):
	# 		self.points[i] = (self.points[i][0] + 1, self.points[i][1])

	# def move_to(self, row, col):
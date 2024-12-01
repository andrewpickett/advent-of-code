from copy import copy


class Point:
	def __init__(self, row, col, value=None):
		self.col = col
		self.row = row
		self.value = value
		self.neighbors = []
		self.visited = False

	def __str__(self):
		return "({},{}):{}".format(self.row, self.col, self.value)

	def __repr__(self):
		return "({},{}):{}".format(self.row, self.col, self.value)

	def __eq__(self, other):
		return self.row == other.row and self.col == other.col

	def __hash__(self):
		return hash(str(self.row) + "_" + str(self.col))

	def __copy__(self):
		p = Point(self.row, self.col, copy(self.value))
		p.visited = self.visited
		return p

	def __iter__(self):
		return iter((self.row, self.col))

	def get_coord(self):
		return self.row, self.col

	def get_row(self):
		return self.row

	def set_row(self, row):
		self.row = row

	def get_col(self):
		return self.col

	def set_col(self, col):
		self.col = col

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def set_neighbors(self, neighbors):
		self.neighbors = neighbors

	def is_visited(self):
		return self.visited

	def set_visited(self, visited):
		self.visited = visited

	def get_neighbors(self):
		return self.neighbors

	def get_north_neighbors(self):
		return [n for n in self.neighbors if n.row == self.row - 1]

	def get_north_neighbor(self):
		return self.get_neighbor((-1, 0))

	def get_south_neighbors(self):
		return [n for n in self.neighbors if n.row == self.row + 1]

	def get_south_neighbor(self):
		return self.get_neighbor((1, 0))

	def get_east_neighbors(self):
		return [n for n in self.neighbors if n.col == self.col + 1]

	def get_east_neighbor(self):
		return self.get_neighbor((0, 1))

	def get_west_neighbors(self):
		return [n for n in self.neighbors if n.col == self.col - 1]

	def get_west_neighbor(self):
		return self.get_neighbor((0, -1))

	def get_neighbor(self, pos):
		ns = [n for n in self.neighbors if n.col == self.col + pos[1] and n.row == self.row + pos[0]]
		if len(ns) > 0:
			return ns[0]


class Grid:
	def __init__(self, height=0, width=0, values=None, default_value="", file=None):
		if file:
			with open(file) as f:
				values = [[y for y in x.strip()] for x in f.readlines()]
		if height > 0 and width > 0 and values:
			raise RuntimeError("Cannot define both the dimensions and default values. One or the other are required.")
		self.data = []
		self.height = height if not values else len(values)
		self.width = width if not values else len(values[0])
		for r in range(self.height):
			row = []
			for c in range(self.width):
				if values and isinstance(values[r][c], Point):
					row.append(copy(values[r][c]))
				else:
					row.append(Point(r, c, default_value if not values else values[r][c]))
			self.data.append(row)
		self.neighbors_set = False
		self.include_diagonals = False

	def set_neighbors_for_point(self, p=None, row=-1, col=-1, include_diagonals=False):
		if not p and row >= 0 and col >= 0:
			p = self.get_point(row, col)
		neighbors = []
		for y in range(-1, 2):
			for x in range(-1, 2):
				if (y == 0 and x == 0) or (abs(y) + abs(x) > 1 and not include_diagonals):
					continue
				if 0 <= p.get_row()+y < len(self.data) and 0 <= p.get_col() + x < len(self.data[p.get_row()]):
					neighbors.append(self.get_point(p.get_row()+y, p.get_col()+x))
		p.set_neighbors(neighbors)
		self.neighbors_set = True
		self.include_diagonals = include_diagonals

	def set_neighbors_for_all(self, include_diagonals=False):
		for row in self.data:
			for col in row:
				self.set_neighbors_for_point(p=col, include_diagonals=include_diagonals)

	def get_row(self, row):
		return self.data[row]

	def get_point(self, row=0, col=0, coords=None):
		return self.data[coords[0]][coords[1]] if coords else self.data[row][col]

	def get_height(self):
		return self.height

	def get_width(self):
		return self.width

	def get_points(self):
		return [pt for row in range(len(self.data)) for pt in self.data[row]]

	def __str__(self):
		out_val = "["
		for row in range(len(self.data)):
			if row > 0:
				out_val += " "
			out_val += "[" + ",".join([str(x.get_value()) for x in self.data[row]]) + "]"
			if row < len(self.data) - 1:
				out_val += "\n"
		out_val += "]"
		return out_val

	def output(self):
		out_val = ""
		for row in range(len(self.data)):
			out_val += "".join([str(x.get_value()) for x in self.data[row]])
			if row < len(self.data) - 1:
				out_val += "\n"
		return out_val

	def __copy__(self):
		g = Grid(values=self.data)
		if self.neighbors_set:
			g.set_neighbors_for_all(self.include_diagonals)
		return g

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
		p = Point(self.row, self.col, self.value)
		p.visited = self.visited
		return p

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
		ns = [n for n in self.neighbors if n.row == self.row - 1 and n.col == self.col]
		if len(ns) > 0:
			return ns[0]

	def get_south_neighbors(self):
		return [n for n in self.neighbors if n.row == self.row + 1]

	def get_south_neighbor(self):
		ns = [n for n in self.neighbors if n.row == self.row + 1 and n.col == self.col]
		if len(ns) > 0:
			return ns[0]

	def get_east_neighbors(self):
		return [n for n in self.neighbors if n.col == self.col + 1]

	def get_east_neighbor(self):
		ns = [n for n in self.neighbors if n.col == self.col + 1 and n.row == self.row]
		if len(ns) > 0:
			return ns[0]

	def get_west_neighbors(self):
		return [n for n in self.neighbors if n.col == self.col - 1]

	def get_west_neighbor(self):
		ns = [n for n in self.neighbors if n.col == self.col - 1 and n.row == self.row]
		if len(ns) > 0:
			return ns[0]

class Grid:
	def __init__(self, height=0, width=0, values=None, default_value=""):
		if height > 0 and width > 0 and values:
			raise RuntimeError("Cannot define both the dimensions and default values. One or the other are required.")
		self.data = []
		self.height = height if not values else len(values)
		self.width = width if not values else len(values[0])
		for r in range(self.height):
			row = []
			for c in range(self.width):
				if isinstance(values[r][c], Point):
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

	def get_col(self, col):
		c_data = []
		for row in self.data:
			c_data.append(row[col])
		return c_data

	def insert_column_after(self, val, n):
		s = len(self.data)
		for i in range(s):
			row = self.data[i]
			row.insert(n, col[i])

	def insert_column_before(self, col, n):
		for i, row in enumerate(self.data):
			row.insert(n-1, col[i])

	def insert_row_before(self, row, n):
		self.data.insert(n-1, row)

	def insert_row_after(self, row, n):
		self.data.insert(n, row)

	def get_point(self, row, col):
		return self.data[row][col]

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

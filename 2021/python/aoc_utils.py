import os, psutil
import time


def run_with_timer(f):
	stime = time.time_ns()
	result = f()
	etime = time.time_ns()
	print("{} -- {} -- took {} ms".format(f.__name__, result, (etime - stime) // 1000000))
	return result


def perf_test(f, runs):
	process = psutil.Process(os.getpid())
	start_mem = process.memory_info().rss
	stime = time.time_ns()
	for i in range(runs):
		result = f()
	etime = time.time_ns()
	end_mem = process.memory_info().rss
	print("{} -- {} -- took {} ns average over {} runs with {} memory".format(f.__name__, result, (etime - stime) // runs, runs, (end_mem - start_mem)))
	return result


class Point:
	def __init__(self, row, col, value=None):
		self.col = col
		self.row = row
		self.value = value
		self.neighbors = []

	def __str__(self):
		return "({},{}):{}".format(self.row, self.col, self.value)

	def __repr__(self):
		return "({},{}):{}".format(self.row, self.col, self.value)

	def __eq__(self, other):
		return self.row == other.row and self.col == other.col

	def __hash__(self):
		return hash(str(self.row) + "_" + str(self.col))

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

	def get_neighbors(self):
		return self.neighbors


class Grid:
	def __init__(self, height=0, width=0, values=None, default_value=""):
		if height > 0 and width > 0 and values:
			raise RuntimeError("Cannot define both the dimensions and default values. One or the other are required.")
			return
		self.data = []
		self.height = height if not values else len(values)
		self.width = width if not values else len(values[0])
		for r in range(self.height):
			row = []
			for c in range(self.width):
				row.append(Point(r, c, default_value if not values else values[r][c]))
			self.data.append(row)

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

	def set_neighbors_for_all(self, include_diagonals=False):
		for row in self.data:
			for col in row:
				self.set_neighbors_for_point(p=col, include_diagonals=include_diagonals)

	def get_row(self, row):
		return self.data[row]

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

from collections import deque
from copy import copy
from typing import Callable, Optional, Self, Iterator, TextIO

from utils.utils import NEIGHBOR_COORDS, ORTHOGONAL, ALL


class Point:
	def __init__(self, row:int, col:int, value:Optional[object]=None) -> None:
		self.col = col
		self.row = row
		self.value = value
		self.neighbors = []
		self.visited = False

	def __str__(self) -> str:
		return "({},{}):{}".format(self.row, self.col, self.value)

	def __repr__(self) -> str:
		return str(self)

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Point):
			return NotImplemented
		return self.row == other.row and self.col == other.col

	def __hash__(self) -> int:
		return hash(str(self))

	def __copy__(self) -> Self:
		p = Point(self.row, self.col, copy(self.value))
		p.visited = self.visited
		return p

	def __iter__(self) -> Iterator[tuple]:
		return iter((self.row, self.col))

	def get_coord(self) -> tuple[int, int]:
		return self.row, self.col

	def get_north_neighbors(self) -> list:
		return [n for n in self.neighbors if n.row == self.row - 1]

	def get_north_neighbor(self) -> Self:
		return self.get_neighbor((-1, 0))

	def get_south_neighbors(self) -> list:
		return [n for n in self.neighbors if n.row == self.row + 1]

	def get_south_neighbor(self) -> Self:
		return self.get_neighbor((1, 0))

	def get_east_neighbors(self) -> list:
		return [n for n in self.neighbors if n.col == self.col + 1]

	def get_east_neighbor(self) -> Self:
		return self.get_neighbor((0, 1))

	def get_west_neighbors(self) -> list:
		return [n for n in self.neighbors if n.col == self.col - 1]

	def get_west_neighbor(self) -> Self:
		return self.get_neighbor((0, -1))

	def get_neighbor(self, pos: tuple) -> Self:
		ns = [n for n in self.neighbors if n.col == self.col + pos[1] and n.row == self.row + pos[0]]
		if len(ns) > 0:
			return ns[0]
		return None

	def get_line(self, pos: tuple, dist: int) -> list:
		curr_point = self
		line = [curr_point]
		for i in range(1, dist):
			ns = [n for n in curr_point.neighbors if n.col == curr_point.col + pos[1] and n.row == curr_point.row + pos[0]]
			if len(ns) > 0:
				curr_point = ns[0]
				line.append(curr_point)
			else:
				break
		return line


class Grid:
	def __init__(self, height: int=0, width: int=0, values:list[list]=None, default_value:object="", filename:Optional[str]=None, file:Optional[TextIO]=None) -> None:
		if filename:
			with open(filename) as f:
				values = [[y for y in x.strip()] for x in f.readlines()]
		elif file:
			values = [[y for y in x.strip()] for x in file.readlines()]

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

	def __str__(self) -> str:
		out_val = "["
		for row in range(len(self.data)):
			if row > 0:
				out_val += " "
			out_val += "[" + ",".join([str(x.value) for x in self.data[row]]) + "]"
			if row < len(self.data) - 1:
				out_val += "\n"
		out_val += "]"
		return out_val

	def __copy__(self) -> Self:
		g = Grid(values=self.data)
		if self.neighbors_set:
			g.set_neighbors_for_all(self.include_diagonals)
		return g

	def set_neighbors_for_point(self, p: Optional[Point]=None, row: int=-1, col: int=-1, include_diagonals: bool=False) -> None:
		if not p and row >= 0 and col >= 0:
			p = self.get_point(row, col)
		neighbors = []
		for y in range(-1, 2):
			for x in range(-1, 2):
				if (y == 0 and x == 0) or (abs(y) + abs(x) > 1 and not include_diagonals):
					continue
				if 0 <= p.row+y < len(self.data) and 0 <= p.col + x < len(self.data[p.row]):
					neighbors.append(self.get_point(p.row+y, p.col+x))
		p.neighbors = neighbors
		self.neighbors_set = True
		self.include_diagonals = include_diagonals

	def set_neighbors_for_all(self, include_diagonals: bool=False) -> None:
		for row in self.data:
			for col in row:
				self.set_neighbors_for_point(p=col, include_diagonals=include_diagonals)

	def get_row(self, row: int) -> list:
		return self.data[row]

	def get_point(self, row: int=0, col: int=0, coords: Optional[tuple]=None) -> Point:
		return self.data[coords[0]][coords[1]] if coords else self.data[row][col]

	def get_points(self) -> list:
		return [pt for row in range(len(self.data)) for pt in self.data[row]]

	def get_neighbor(self, pt: Point, n: tuple) -> Optional[Point]:
		np = (pt.row + n[0], pt.col + n[1])
		return None if (np[0] < 0 or np[0] >= len(self.data) or np[1] < 0 or np[1] >= len(self.data[pt.row])) else self.get_point(coords=np)

	def get_neighbors(self, pt: Point, include_diagonals: bool=False) -> list:
		ns = []
		for n in (NEIGHBOR_COORDS[ORTHOGONAL] if not include_diagonals else NEIGHBOR_COORDS[ALL]):
			neighbor = self.get_neighbor(pt, n)
			if neighbor:
				ns.append(neighbor)
		return ns

	def output(self) -> str:
		out_val = ""
		for row in range(len(self.data)):
			out_val += "".join([str(x.value) for x in self.data[row]])
			if row < len(self.data) - 1:
				out_val += "\n"
		return out_val


def bfs(grid: Grid, src: Point, dest: Point, neighbor_func: Callable[[Grid, Point], list[Point]]=lambda g, p: g.get_neighbors(p), inc_func: Callable[[Point], int]=lambda _: 1) -> Optional[tuple]:
	"""
	Simple BFS algorithm that takes a "source" object, a "destination" and finds the shortest path from src to dest.
	:param grid: The grid we're traversing with a BFS
	:param src: Some object that is the source
	:param dest: Some object that is the destination
	:param neighbor_func: The function that should be called to determine neighbors of a given "point"
	:param inc_func: Optional increment function that determines how much to increment the value. This basically allows for weighted distances between nodes. By default, the value is just 1
	:return: a tuple containing the destination point, the distance to get to that point, and the parent (which can be used to trace all the way back to the source)
	"""
	a: tuple[Point, int, Optional[tuple]] = (src, 0, None)
	visited: set[Point] = set()
	visited.add(a[0])
	q = deque([a])
	while q:
		curr = q.popleft()
		if curr[0] == dest:
			return curr
		for x in neighbor_func(grid, curr[0]):
			if x not in visited:
				a = (x, curr[1] + inc_func(x), curr)
				visited.add(a[0])
				q.append(a)
	return None


def reconstruct_path(came_from: dict, current: Point) -> list:
	total_path = [current]
	while current in came_from.keys():
		current = came_from[current]
		total_path.insert(0, current)
	return total_path


def astar(grid: Grid, src: Point, dest: Point, early_exit: bool=True, h:Callable[[Point], float]=lambda x: 0) -> Optional[list]:
	open_set = [src]
	came_from = {}

	g_score = {src: 0.0}
	f_score = {src: h(src)}

	while len(open_set) > 0:
		min_val = float("inf")
		min_x = None
		for x in open_set:
			if x in f_score and f_score[x] < min_val:
				min_val = f_score[x]
				min_x = x
		current = min_x

		if early_exit and current == dest:
			return reconstruct_path(came_from, current)

		open_set.remove(current)
		for neighbor in [x for x in grid.get_neighbors(current) if x.value != "#"]:
			tentative_g_score = g_score[current] + 1
			if neighbor not in g_score:
				g_score[neighbor] = float("inf")
			if neighbor not in f_score:
				f_score[neighbor] = float("inf")
			if tentative_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score[neighbor] = tentative_g_score + h(neighbor)
				if neighbor not in open_set:
					open_set.append(neighbor)
	return None

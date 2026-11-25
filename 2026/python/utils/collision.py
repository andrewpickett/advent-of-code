from typing import Self


class Point2d:
	"""A simple object to contain xy-coordinates to represent a point in 2d space.
	"""

	def __init__(self, x: int, y: int) -> None:
		"""Construct a new `Point2d` object with the `x` and `y` coordinates defined.

		Attributes:
			x (int): The x-coordinate for this given point.
			y (int): The y-coordinate for this given point.
		"""
		self.x = x
		self.y = y

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Point2d):
			return False
		return self.x == other.x and self.y == other.y

	def __repr__(self) -> str:
		return "Point2d({}, {})".format(self.x, self.y)

	def __str__(self) -> str:
		return "({}, {})".format(self.x, self.y)


class Line2d:
	"""A simple object to represent a line in 2d space with given start and end points.
	"""

	def __init__(self, start: Point2d, end: Point2d) -> None:
		"""Construct a new `Line2d` object with a given start and end point.

		Attributes:
			start (Point2d): The `Point2d` object representing the start point of the line.
			end (Point2d): The `Point2d` object representing the end point of the line.
		"""
		self.start = start
		self.end = end

	def check_intersection(self, other: Self) -> bool:
		"""Checks if the current `Line2d` intersects the given `Line2d` instance at any given point.

		This method uses a set of four 'orientation' checks to determine if the start/end point of each line segment
		are on opposite sides of the other line segment. You can read more details by looking up the "orientation
		algorithm for intersecting line segments". Once the orientations of all 4 points are calculated wrt the opposing
		segments, it can be determined if they intersect by checking if they are on opposite sides of the line (their
		orientation product would be negative).

		Attributes:
			other (Line2d): The other `Line2d` instance on which to check intersection on.
		Returns:
			True if this line intersects the given line, False otherwise.
		"""
		o1 = self._orientation(other.start)
		o2 = self._orientation(other.end)
		o3 = other._orientation(self.start)
		o4 = other._orientation(self.end)
		return o1 * o2 < 0 and o3 * o4 < 0


	def _orientation(self, other_pt: Point2d) -> int:
		# A point can either be collinear (0), clockwise (1), or counter-clockwise (-1) of a segment.
		v = (self.end.x - self.start.x) * (other_pt.y - self.start.y) - (self.end.y - self.start.y) * (other_pt.x - self.start.x)
		return 1 if v > 0 else (-1 if v < 0 else 0)


	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Line2d):
			return False
		return self.start == other.start and self.end == other.end


	def __repr__(self) -> str:
		return "Line2d({} --> {})".format(self.start, self.end)


	def __str__(self) -> str:
		return "{} --> {}".format(self.start, self.end)


class BoundingBox:
	"""A class that defines a rectangular area in a 2d space by defining two opposite points of that space.
	"""

	def __init__(self, pt1: Point2d, pt2: Point2d) -> None:
		"""Construct a new `BoundingBox` by defining two points on opposite corners of the desired area.

		This will define the x and y ranges of the resulting 2d box as well as define the four corners and the four edges.

		Attributes:
			pt1 (Point2d): The first corner point of the box.
			pt2 (Point2d): The second corner point of the box.
		"""
		self.xrange = range(min(pt1.x, pt2.x), max(pt1.x, pt2.x))
		self.yrange = range(min(pt1.y, pt2.y), max(pt1.y, pt2.y))
		self.bounds = {
			"ul": Point2d(self.xrange.start, self.yrange.start),
			"ur": Point2d(self.xrange.stop, self.yrange.start),
			"bl": Point2d(self.xrange.start, self.yrange.stop),
			"br": Point2d(self.xrange.stop, self.yrange.stop)
		}
		self.edges = {
			"top": Line2d(self.bounds["ul"], self.bounds["ur"]),
			"bottom": Line2d(self.bounds["bl"], self.bounds["br"]),
			"left": Line2d(self.bounds["ul"], self.bounds["bl"]),
			"right": Line2d(self.bounds["ur"], self.bounds["br"]),
		}


	def area(self) -> int:
		"""Calculates the area of the box.
		"""
		return (self.xrange.stop - self.xrange.start + 1) * (self.yrange.stop - self.yrange.start + 1)


	def __eq__(self, other: object) -> bool:
		if not isinstance(other, BoundingBox):
			return False
		return self.xrange == other.xrange and self.yrange == other.yrange


	def __repr__(self) -> str:
		return "BoundingBox({})".format(self.bounds)


	def __str__(self) -> str:
		return "{}".format(self.bounds)

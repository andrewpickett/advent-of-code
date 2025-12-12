from typing import cast

class Point2d:
	def __init__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y

	def __repr__(self) -> str:
		return "({}, {})".format(self.x, self.y)


class Line2d:
	def __init__(self, start: Point2d, end: Point2d) -> None:
		self.start = start
		self.end = end

	def check_intersection(self, other: object) -> bool:
		o = cast(Line2d, other)
		o1 = Line2d._orientation(self.start, self.end, o.start)
		o2 = Line2d._orientation(self.start, self.end, o.end)
		o3 = Line2d._orientation(o.start, o.end, self.start)
		o4 = Line2d._orientation(o.start, o.end, self.end)
		return o1 * o2 < 0 and o3 * o4 < 0

	@staticmethod
	def _orientation(pt1: Point2d, pt2: Point2d, pt3: Point2d) -> int:
		v = (pt2.x - pt1.x) * (pt3.y - pt1.y) - (pt2.y - pt1.y) * (pt3.x - pt1.x)
		if v > 0:
			return 1
		if v < 0:
			return -1
		return 0

	def __repr__(self) -> str:
		return "{} -- {}".format(self.start, self.end)


class BoundingBox:
	def __init__(self, pt1: Point2d, pt2: Point2d) -> None:
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
		return (self.xrange.stop - self.xrange.start + 1) * (self.yrange.stop - self.yrange.start + 1)

	def __repr__(self) -> str:
		return "ul: {}, ur: {}, bl: {}, br: {}".format(self.bounds["ul"], self.bounds["ur"], self.bounds["bl"], self.bounds["br"])

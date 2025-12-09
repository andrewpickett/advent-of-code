class Point2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "({}, {})".format(self.x, self.y)


def _orientation(pt1, pt2, pt3):
	v = (pt2.x - pt1.x) * (pt3.y - pt1.y) - (pt2.y - pt1.y) * (pt3.x - pt1.x)
	if v > 0:
		return 1
	if v < 0:
		return -1
	return 0


class Line2d:

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def check_intersection(self, other):
		o1 = _orientation(self.start, self.end, other.start)
		o2 = _orientation(self.start, self.end, other.end)
		o3 = _orientation(other.start, other.end, self.start)
		o4 = _orientation(other.start, other.end, self.end)
		return o1 * o2 < 0 and o3 * o4 < 0

	def __repr__(self):
		return "{} -- {}".format(self.start, self.end)


class BoundingBox:
	def __init__(self, pt1, pt2):
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

	def area(self):
		return (self.xrange.stop - self.xrange.start + 1) * (self.yrange.stop - self.yrange.start + 1)

	def __repr__(self):
		return "ul: {}, ur: {}, bl: {}, br: {}".format(self.bounds["ul"], self.bounds["ur"], self.bounds["bl"], self.bounds["br"])

from utils.collision import Point2d, BoundingBox, Line2d
from utils.timers import run_with_timer, get_data_with_timer


def get_data(f):
	return [Point2d(*list(map(int, x.strip().split(",")))) for x in f.readlines()]


def part_one(d):
	return max(abs(d[x].x - d[y].x + 1) * abs(d[x].y - d[y].y + 1) for x in range(len(d) - 1) for y in range(len(d)))


def part_two(d):
	best = 0
	for i in range(len(d) - 1):
		for j in range(i + 1, len(d)):
			box = BoundingBox(d[i], d[j])
			if box_in_polygon(box, d):
				area = box.area()
				if area > best:
					best = area
	return best


def box_in_polygon(box, polygon):
	for pt in box.bounds.values():
		if not point_in_polygon(pt, polygon):
			return False
	n = len(polygon)
	for edge in box.edges.values():
		for i in range(n):
			poly_edge = Line2d(polygon[i], polygon[(i + 1) % n])
			if edge.check_intersection(poly_edge):
				return False
	return True


def point_in_polygon(pt, polygon):
	inside = False
	n = len(polygon)
	for i in range(n):
		segment = Line2d(polygon[i], polygon[(i + 1) % n])
		if point_on_segment(pt, segment):
			return True
		if (segment.start.y > pt.y) != (segment.end.y > pt.y):
			x_intersect = (segment.end.x - segment.start.x) * (pt.y - segment.start.y) / (segment.end.y - segment.start.y) + segment.start.x
			if pt.x < x_intersect:
				inside = not inside
	return inside


def point_on_segment(pt, segment):
	cross = (segment.end.x - segment.start.x) * (pt.y - segment.start.y) - (segment.end.y - segment.start.y) * (pt.x - segment.start.x)
	if abs(cross) > 0:
		return False
	if not (min(segment.start.x, segment.end.x) <= pt.x <= max(segment.start.x, segment.end.x) and
			  min(segment.start.y, segment.end.y) <= pt.y <= max(segment.start.y, segment.end.y)):
		return False
	return True


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

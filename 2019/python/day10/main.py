from fractions import Fraction
from itertools import cycle
import math

data = [x.strip() for x in open("input.txt").readlines()]

points = []
point_line_map = {}


def part_one():
	max_val = 0
	max_pos = (0, 0)
	for point in point_line_map:
		if len(point_line_map[point]) > max_val:
			max_val = len(point_line_map[point])
			max_pos = point
	return max_val, max_pos


def part_two():
	base_point = (26, 36,)
	remaining_targets = list(points)
	remaining_targets.remove(base_point)
	lines_of_sight = list(set((x[0], x[1],) for x in list(point_line_map[base_point])))
	lines_of_sight.sort()
	lines_of_sight.insert(0, lines_of_sight.pop(-1))
	counter = 0
	x_increase = False
	asteroids_destroyed = []
	for line in cycle(lines_of_sight):
		if not remaining_targets:
			break

		if line[0] == math.inf:
			x_increase = not x_increase

		new_point = get_next_point_on_line((base_point[0], base_point[1],), line[0], x_increase)
		while 0 <= new_point[1] < len(data) and 0 <= new_point[0] < len(data):
			if destroy_asteroid_if_found(new_point, remaining_targets, asteroids_destroyed):
				counter += 1
				break
			new_point = get_next_point_on_line(new_point, line[0], x_increase)
	return asteroids_destroyed[199][0] * 100 + asteroids_destroyed[199][1]


def get_next_point_on_line(curr_point, slope, x_increase):
	if slope == math.inf:
		return curr_point[0], curr_point[1] + (1 if not x_increase else -1),
	else:
		xfact = -1 if not x_increase else 1
		return curr_point[0] + (slope.denominator * xfact), curr_point[1] + (slope.numerator * xfact),


def destroy_asteroid_if_found(asteroid, remaining_targets, asteroids_destroyed):
	if asteroid in remaining_targets:
		remaining_targets.remove(asteroid)
		asteroids_destroyed.append(asteroid)
		return True
	return False


def build_point_list():
	points_list = []
	for i, line in enumerate(data):
		for j, pos in enumerate(line):
			if pos == '#':
				points_list.append((j, i,))
	return points_list


def build_point_line_map():
	tots = dict()
	for start_point in points:
		tots[start_point] = set()
		for end_point in set(points) - {start_point}:
			if start_point[0] == end_point[0]:
				equation = (math.inf, None, (end_point[1] < start_point[1]),)
			elif start_point[1] == end_point[1]:
				equation = (0, start_point[1], (end_point[0] < start_point[0]),)
			else:
				slope = Fraction(end_point[1] - start_point[1], end_point[0] - start_point[0])
				yint = start_point[1] - (start_point[0] * slope)
				equation = (slope, yint, ((slope < 0 and end_point[1] > start_point[1]) or (slope > 0 and end_point[1] < start_point[1])),)
			tots[start_point].add(equation)
	return tots


if __name__ == '__main__':
	points = build_point_list()
	point_line_map = build_point_line_map()
	print(part_one())  # 347
	print(part_two())  # 829

import sys

from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	wire_1_coords = populate_wire_coords(data[0].split(','))
	wire_2_coords = populate_wire_coords(data[1].split(','))
	closest_intersection = find_closest_intersection(wire_1_coords, wire_2_coords)

	return abs(closest_intersection[0][0]) + abs(closest_intersection[0][1])


def part_two():
	wire_1_coords = populate_wire_coords(data[0].split(','))
	wire_2_coords = populate_wire_coords(data[1].split(','))
	intersections = find_intersections(wire_1_coords, wire_2_coords)

	intersection_distances = []
	for intersection in intersections:
		wire_1_distance = calculate_total_distance_travelled(wire_1_coords, intersection, 1)
		wire_2_distance = calculate_total_distance_travelled(wire_2_coords, intersection, 2)
		intersection_distances.append(wire_1_distance + wire_2_distance)

	return min(intersection_distances)


def populate_wire_coords(moves):
	curr_pos = (0, 0)
	wire = [curr_pos]
	for move in moves:
		direction = move[0:1]
		magnitude = int(move[1:])
		magnitude = magnitude * -1 if direction == 'D' or direction == 'L' else magnitude

		curr_pos = (curr_pos[0] + magnitude, curr_pos[1]) if direction == 'L' or direction == 'R' else (curr_pos[0], curr_pos[1] + magnitude)
		wire.append(curr_pos)
	return wire


def calculate_total_distance_travelled(wire_coords, end_point, end_point_idx):
	wire_distance = 0
	for i in range(0, end_point[end_point_idx]):
		wire_distance += calculate_manhattan_distance(wire_coords[i], wire_coords[i + 1])
	wire_distance += calculate_manhattan_distance(wire_coords[end_point[end_point_idx]], end_point[0])
	return wire_distance


def calculate_manhattan_distance(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_intersections(wire_1_coords, wire_2_coords):
	intersections = []

	for i in range(0, len(wire_1_coords) - 1):
		for j in range(0, len(wire_2_coords) - 1):
			crossing_point = determine_crossing(wire_1_coords[i], wire_1_coords[i + 1], wire_2_coords[j], wire_2_coords[j + 1])
			if crossing_point and crossing_point != (0, 0):
				intersections.append((crossing_point, i, j))
	return intersections


def find_closest_intersection(wire_1_coords, wire_2_coords):
	intersections = find_intersections(wire_1_coords, wire_2_coords)

	min_distance = sys.maxsize
	min_dist_coord = None
	for intersection in intersections:
		dist = abs(intersection[0][0]) + abs(intersection[0][1])
		if dist < min_distance:
			min_distance = dist
			min_dist_coord = intersection
	return min_dist_coord


def determine_crossing(w1_start, w1_end, w2_start, w2_end):
	horiz_line = (w2_start, w2_end) if w1_start[0] == w1_end[0] else (w1_start, w1_end)
	vert_line = (w2_start, w2_end) if w1_start[1] == w1_end[1] else (w1_start, w1_end)

	x_vals = [horiz_line[0][0], horiz_line[1][0]]
	y_vals = [vert_line[0][1], vert_line[1][1]]
	if vert_line[0][0] in range(min(x_vals), max(x_vals)) and horiz_line[0][1] in range(min(y_vals), max(y_vals)):
		return vert_line[0][0], horiz_line[0][1]
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 2129
	run_with_timer(part_two)  # 134662

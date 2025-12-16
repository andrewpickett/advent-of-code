from aoc_utils import run_with_timer, Grid
import re

data = [x.strip("\n") for x in open("input.txt").readlines()]

dirs = {
	0: (0, 1),
	1: (1, 0),
	2: (0, -1),
	3: (-1, 0)
}

row_boundaries = {}
col_boundaries = {}


def parse_data():
	insts = re.findall("\d+[LR]", data[-1])
	instructions = []
	for i in insts:
		instructions.append((int(i[:-1]), i[-1]))
	total_cols = max(len(x) for x in data[:-2])
	new_data = []
	for x in data[:-2]:
		new_data.append(x.ljust(total_cols, " "))

	# Get "boundaries" for each row's data
	for row, x in enumerate(new_data):
		left_boundary = x.find(".") if x.find("#") == -1 else min(x.find("."), x.find("#"))
		right_boundary = left_boundary + len(x.strip())
		row_boundaries[row] = (left_boundary, right_boundary)
	# Get "boundaries for each column's data
	for col in range(total_cols):
		found = False
		for row, x in enumerate(new_data):
			if x[col] != " " and col not in col_boundaries:
				col_boundaries[col] = row
			elif x[col] == " " and col in col_boundaries:
				col_boundaries[col] = (col_boundaries[col], row-1)
				found = True
				break
		if not found:
			col_boundaries[col] = (col_boundaries[col], len(new_data)-1)

	return instructions, Grid(values=new_data)


def get_next_point_2d(g, curr_point, curr_dir):
	next_point_pos = (curr_point.get_row()+dirs[curr_dir][0], curr_point.get_col()+dirs[curr_dir][1])
	if curr_dir == 0:
		if next_point_pos[1] >= row_boundaries[curr_point.get_row()][1]:
			next_point_pos = (next_point_pos[0], row_boundaries[curr_point.get_row()][0])
	elif curr_dir == 1:
		if next_point_pos[0] > col_boundaries[curr_point.get_col()][1]:
			next_point_pos = (col_boundaries[curr_point.get_col()][0], next_point_pos[1])
	elif curr_dir == 2:
		if next_point_pos[1] < row_boundaries[curr_point.get_row()][0]:
			next_point_pos = (next_point_pos[0], row_boundaries[curr_point.get_row()][1]-1)
	elif curr_dir == 3:
		if next_point_pos[0] < col_boundaries[curr_point.get_col()][0]:
			next_point_pos = (col_boundaries[curr_point.get_col()][1], next_point_pos[1])
	return g.get_point(next_point_pos[0], next_point_pos[1])


def get_next_point_3d(g, curr_point, curr_dir):
	return g.get_point(curr_point.get_row(), curr_point.get_col(),), curr_dir


def part_one():
	instructions, g = parse_data()
	curr_point = g.get_point(0, data[0].find("."))
	curr_dir = 0
	for i in instructions:
		for j in range(i[0]):
			next_point = get_next_point_2d(g, curr_point, curr_dir)
			if next_point.get_value() == "#":
				break
			else:
				curr_point = next_point
		curr_dir = (curr_dir + (1 if i[1] == "R" else -1)) % len(dirs)
	return sum([1000*(curr_point.get_row()+1), 4*(curr_point.get_col()+1), curr_dir])


def part_two():
	instructions, g = parse_data()
	curr_point = g.get_point(0, data[0].find("."))
	curr_dir = 0
	for i in instructions:
		for j in range(i[0]):
			next_point, next_dir = get_next_point_3d(g, curr_point, curr_dir)
			if next_point.get_value() == "#":
				break
			else:
				curr_point = next_point
		curr_dir = (next_dir + (1 if i[1] == "R" else -1)) % len(dirs)
	return sum([1000*(curr_point.get_row()+1), 4*(curr_point.get_col()+1), curr_dir])


if __name__ == '__main__':
	run_with_timer(part_one)  # 55244 -- took 62 ms
	run_with_timer(part_two)  #
#123149

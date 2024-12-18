from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.utils import DIRS, turn_around
from collections import deque
from copy import deepcopy

def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	directions = False
	gridlines = []
	ds = ""
	for line in lines:
		if line == "":
			directions = True
			continue
		if directions:
			ds += line
		else:
			gridlines.append(line)
	g = Grid(values=gridlines)
	return {"directions": ds, "grid": g, "start": [x for x in g.get_points() if x.get_value() == "@"][0]}


def part_one(d):
	grid = d["grid"]
	curr_pt = d["start"]
	run_directions(grid, d["directions"], curr_pt)
	return sum(100*p.get_row() + p.get_col() for p in grid.get_points() if p.get_value() == "O")


def part_two(d):
	grid = double_grid(d["grid"])
	curr_pt = [p for p in grid.get_points() if p.get_value() == "@"][0]
	run_directions(grid, d["directions"], curr_pt)
	return sum(100*p.get_row() + p.get_col() for p in grid.get_points() if p.get_value() == "[")


def get_line(grid, curr_pt, direction, line, included_pts):
	q = deque([curr_pt])
	while q:
		p = q.popleft()
		included_pts.add(p)
		prev_node = grid.get_neighbor(p, turn_around(DIRS[direction]))
		prev_val = "." if p.get_value() in ["@", "#"] or prev_node not in included_pts else grid.get_neighbor(p, turn_around(DIRS[direction])).get_value()
		line.append((p, prev_val))
		if p.get_value() != ".":
			adj = grid.get_neighbor(p, DIRS[direction])
			if adj not in q:
				q.append(adj)
			if adj.get_value() == "#":
				return False
			if adj.get_value() != ".":
				if adj.get_value() == "[":
					other_box = grid.get_neighbor(adj, DIRS[">"])
					if other_box not in included_pts:
						q.append(other_box)
				elif adj.get_value() == "]":
					other_box = grid.get_neighbor(adj, DIRS["<"])
					if other_box not in included_pts:
						q.append(other_box)
	return True


def move(line):
	for l in line:
		l[0].set_value(l[1])
	return line[1][0]


def run_directions(grid, directions, curr_pt):
	for direction in directions:
		adj_pt = grid.get_neighbor(curr_pt, DIRS[direction])
		if adj_pt.get_value() != "#":
			if adj_pt.get_value() == ".":
				curr_pt.set_value(".")
				adj_pt.set_value("@")
				curr_pt = adj_pt
			else:
				line = []
				included_pts = set()
				if get_line(grid, curr_pt, direction, line, included_pts):
					curr_pt = move(line)


def double_grid(grid):
	new_g = []
	for row in grid.data:
		new_row = []
		for col in row:
			if col.get_value() == "#":
				new_row.append("#")
				new_row.append("#")
			elif col.get_value() == "O":
				new_row.append("[")
				new_row.append("]")
			elif col.get_value() == ".":
				new_row.append(".")
				new_row.append(".")
			else:
				new_row.append("@")
				new_row.append(".")
		new_g.append(new_row)
	return Grid(values=new_g)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, deepcopy(data))
	run_with_timer(part_two, deepcopy(data))


if __name__ == '__main__':
	main()

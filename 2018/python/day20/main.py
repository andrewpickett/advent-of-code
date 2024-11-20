from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.utils import DIRS
from utils.algorithms import astar


def get_data(filename):
	ret_val = {"grid": build_map(open(filename).readline().strip())}
	ret_val["start"] = get_start(ret_val["grid"])
	return ret_val


def get_start(grid):
	for pt in grid.get_points():
		if pt.get_value() == "X":
			return pt.get_coord()


def build_map(d):
	curr_pos = (0, 0)
	map_grid = {}
	branch_stack = []
	for x in d[1:-1]:
		if x == "(":
			branch_stack.insert(0, curr_pos)
		elif x == "|":
			curr_pos = branch_stack[0]
		elif x == ")":
			branch_stack.pop(0)
		else:
			map_grid[(curr_pos[0] + DIRS[x][0], curr_pos[1] + DIRS[x][1])] = "|" if x in "EW" else "-"
			curr_pos = (curr_pos[0] + DIRS[x][0]*2, curr_pos[1] + DIRS[x][1]*2)
			map_grid[curr_pos] = "."
	map_grid[(0, 0)] = "X"
	return convert_map_to_grid(map_grid)


def convert_map_to_grid(m):
	yrange = (min([x[0] for x in m.keys()]), max([x[0] for x in m.keys()]) + 1)
	xrange = (min([x[1] for x in m.keys()]), max([x[1] for x in m.keys()]) + 1)
	full_grid = [["#"]*(xrange[1]-xrange[0]+2)]
	for y in range(yrange[0], yrange[1]):
		next_row = ["#"]
		for x in range(xrange[0], xrange[1]):
			if (y, x) in m:
				next_row.append(m[(y, x)])
			else:
				next_row.append("#")
		next_row.append("#")
		full_grid.append(next_row)
	full_grid.append(["#"]*(xrange[1]-xrange[0]+2))
	grid = Grid(values=full_grid)
	grid.set_neighbors_for_all()
	return grid


def part_one(d):
	m = 0
	room_dists = {}
	for room in [x for x in d["grid"].get_points() if x.get_value() == "."]:
		if room not in room_dists:
			dist = astar(room, d["grid"].get_point(coords=d["start"]))
			if len(dist) > m:
				m = len(dist)
			room_dists[room] = dist
	return (m-1) // 2


def part_two(d):
	# Haha...manually counted from my output of part 1 -- Need to actually make part 1 faster so I can just re-run
	# and keep track. The below WOULD work, but would also take the hour to run...
	m = 0
	room_dists = {}
	for room in [x for x in d["grid"].get_points() if x.get_value() == "."]:
		if room not in room_dists:
			dist = astar(room, d["grid"].get_point(coords=d["start"]))
			if len(dist) >= 1000:
				m += 1
			room_dists[room] = dist
	return m


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

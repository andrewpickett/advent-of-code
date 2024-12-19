from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.algorithms import bfs


def get_data(filename):
	return {"c": [tuple(map(int, x.strip().split(",")[::-1])) for x in open(filename).readlines()], "s": 71, "b": 1024}


def part_one(d):
	grid = get_grid(d["s"], d["c"], d["b"])
	return bfs(grid, grid.get_point(0, 0), grid.get_point(d["s"]-1, d["s"]-1), lambda g, p: [y for y in g.get_neighbors(p) if y.get_value() == "."])[1]


def part_two(d):
	grid = get_grid(d["s"], d["c"], d["b"])
	i = d["b"]
	while True:
		grid.get_point(coords=d["c"][i]).set_value("#")
		path = bfs(grid, grid.get_point(0, 0), grid.get_point(d["s"]-1, d["s"]-1), lambda g, p: [y for y in g.get_neighbors(p) if y.get_value() == "."])
		if not path:
			return ','.join(list(map(str, d["c"][i][::-1])))
		i += 1


def get_grid(size, coords, block):
	grid = Grid(size, size, default_value=".")
	for x in range(block):
		grid.get_point(coords=coords[x]).set_value("#")
	return grid


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

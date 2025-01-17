from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import get_2d_array
from math import prod
from copy import deepcopy


def get_data(filename):
	lines = [x.strip().split() for x in open(filename).readlines()]
	return {"robots": [{"pos": tuple([int(y) for y in x[0][2:].split(",")]), "vel": tuple([int(y) for y in x[1][2:].split(",")])} for x in lines], "range": (103, 101)}


def get_quads(grid):
	quad1 = sum(grid[y][x] for y in range(0, len(grid) // 2) for x in range(0, len(grid[0]) // 2))
	quad2 = sum(grid[y][x] for y in range((len(grid) // 2) + 1, len(grid)) for x in range(0, len(grid[0]) // 2))
	quad3 = sum(grid[y][x] for y in range(0, len(grid) // 2) for x in range((len(grid[0]) // 2) + 1, len(grid[0])))
	quad4 = sum(grid[y][x] for y in range((len(grid) // 2) + 1, len(grid)) for x in range((len(grid[0]) // 2) + 1, len(grid[0])))
	return quad1, quad2, quad3, quad4


def part_one(d):
	return prod(get_quads(populate_grid_and_move(d, 100, 0, lambda x: x + 1)))


def part_two(d):
	i = 1
	while True:
		grid = populate_grid_and_move(d, 1, ".", lambda x: "#")
		for row in grid:
			if ''.join(row).find("########") >= 0:
				return i
		i += 1


def populate_grid_and_move(d, time, fill_char, robot_func):
	grid = get_2d_array(d["range"][0], d["range"][1], fill_char)
	move(d["robots"], time, d["range"][0], d["range"][1])
	for i, robot in enumerate(d["robots"]):
		grid[robot["pos"][1]][robot["pos"][0]] = robot_func(grid[robot["pos"][1]][robot["pos"][0]])
	return grid


def move(d, time, height, width):
	for robot in d:
		robot["pos"] = ((robot["pos"][0] + time*robot["vel"][0]) % width,(robot["pos"][1] + time*robot["vel"][1]) % height)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, deepcopy(data))
	run_with_timer(part_two, deepcopy(data))


if __name__ == '__main__':
	main()

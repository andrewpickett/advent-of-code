from matplotlib.colors import ListedColormap, BoundaryNorm

from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import get_2d_array
from copy import deepcopy

import matplotlib.pyplot as plt


def get_data(filename):
	lines = [x.strip().split() for x in open(filename).readlines()]
	return {"robots": [{"pos": tuple([int(y) for y in x[0][2:].split(",")]), "vel": tuple([int(y) for y in x[1][2:].split(",")])} for x in lines], "range": (103, 101)}


def draw_dividers(grid):
	for y, row in enumerate(grid):
		grid[y][len(row)//2] = 100
	row = len(grid) // 2
	for x in range(len(grid[row])):
		grid[row][x] = 100


def get_quads(grid):
	quad1 = eval_quad(grid, range(0, len(grid) // 2), range(0, len(grid[0]) // 2))
	quad2 = eval_quad(grid, range((len(grid) // 2) + 1, len(grid)), range(0, len(grid[0]) // 2))
	quad3 = eval_quad(grid, range(0, len(grid) // 2), range((len(grid[0]) // 2) + 1, len(grid[0])))
	quad4 = eval_quad(grid, range((len(grid) // 2) + 1, len(grid)), range((len(grid[0]) // 2) + 1, len(grid[0])))
	return quad1, quad2, quad3, quad4


def draw_part1_with_delay(d, start, end, delay):
	for x in range(start, end):
		ax.clear()
		grid = populate_grid_and_move(d, 1, 0, lambda x: x + 1)
		quad1, quad2, quad3, quad4 = get_quads(grid)
		draw_dividers(grid)
		ax.imshow(grid, cmap=cmap, norm=norm)
		ax.set_title(str(x+1) + " seconds\nQuadrant 1: " + str(quad1) + "\nQuadrant 2: " + str(quad2) + "\nQuadrant 3: " + str(quad3) + "\nQuadrant 4: " + str(quad4) + "\nSafety Factor: " + str(quad1*quad2*quad3*quad4))
		plt.pause(delay)


def part_one(d):
	grid = populate_grid_and_move(d, 0, 0, lambda x: x + 1)
	ax.imshow(grid, cmap=cmap, norm=norm)
	ax.set_title("0 seconds\nQuadrant 1: -\nQuadrant 2: -\nQuadrant 3: -\nQuadrant 4: -\nSafety Factor: -")
	plt.waitforbuttonpress()
	quad1, quad2, quad3, quad4 = get_quads(grid)
	draw_dividers(grid)
	ax.imshow(grid, cmap=cmap, norm=norm)
	ax.set_title("0 seconds\nQuadrant 1: " + str(quad1) + "\nQuadrant 2: " + str(quad2) + "\nQuadrant 3: " + str(quad3) + "\nQuadrant 4: " + str(quad4) + "\nSafety Factor: " + str(quad1*quad2*quad3*quad4))
	plt.waitforbuttonpress()
	draw_part1_with_delay(d, 0, 10, 1)
	draw_part1_with_delay(d, 10, 100, 0.01)
	plt.pause(2)


def part_two(d):
	i = 1
	states = []
	running = True
	while running:
		grid = populate_grid_and_move(d, 1, 0, lambda x: 1)
		e = calc_entropy(grid)
		states.append((grid, e > 0.33, round(e, 2)))
		if e > 0.5:
			break
		if running:
			i += 1

	plt.waitforbuttonpress()
	run_vis(states)
	return i


def populate_grid_and_move(d, time, fill_char, robot_func):
	grid = get_2d_array(d["range"][0], d["range"][1], fill_char)
	move(d["robots"], time, d["range"][0], d["range"][1])
	for i, robot in enumerate(d["robots"]):
		grid[robot["pos"][1]][robot["pos"][0]] = robot_func(grid[robot["pos"][1]][robot["pos"][0]])
	return grid


def move(d, time, height, width):
	for robot in d:
		robot["pos"] = ((robot["pos"][0] + time*robot["vel"][0]) % width,(robot["pos"][1] + time*robot["vel"][1]) % height)


def eval_quad(grid, yrange, xrange):
	return sum(grid[y][x] for y in yrange for x in xrange)


def calc_entropy(grid):
	total_connected = 0
	total_points = 0
	for y, row in enumerate(grid):
		for x, col in enumerate(row):
			if col == 1:
				total_points += 1
				if (x > 0 and grid[y][x-1] == 1) or (x < len(row) - 1 and grid[y][x+1] == 1) or (y > 0 and grid[y-1][x] == 1) or (y < len(grid) - 1 and grid[y+1][x] == 1):
					total_connected += 1
	return total_connected / total_points


def run_exmaple(d, title, l=False):
	grid = populate_grid_and_move(d, 0, 0, lambda y: y + 1)
	ax.imshow(grid, cmap=cmap, norm=norm)
	ax.set_title(title + "\n0 seconds")
	plt.waitforbuttonpress()
	for x in range(5):
		grid = populate_grid_and_move(d, 1, 0, lambda y: y + 1)
		ax.clear()
		ax.imshow(grid, cmap=cmap, norm=norm)
		ax.set_title(title + "\n" + str(x+1) + " seconds")
		plt.pause(1)
	if l:
		plt.waitforbuttonpress()
		for x in range(5, 100):
			grid = populate_grid_and_move(d, 1, 0, lambda y: y + 1)
			ax.clear()
			ax.imshow(grid, cmap=cmap, norm=norm)
			ax.set_title(title + "\n" + str(x+1) + " seconds")
			plt.pause(0.05)
	plt.waitforbuttonpress()


def main(f="input.txt"):
	run_exmaple({"robots": [{"pos": (2,4), "vel": (2,-3)}], "range": (7, 11)}, "BASIC MOVEMENT EXAMPLE\nPosition: (2, 4)\nVelocity: (2, -3)")
	sample = get_data_with_timer(get_data, "sample.txt")
	sample["range"] = (7, 11)
	run_exmaple(sample, "FULL EXAMPLE MOVEMENT", True)

	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, deepcopy(data))
	run_with_timer(part_two, deepcopy(data))


def run_vis(states):
	run_display(states[0:10], 1, 0)
	plt.waitforbuttonpress()
	run_display(states[10:99], 0.05, 10)
	plt.waitforbuttonpress()
	run_only_key(states[99:7360], 0.3, 99)
	plt.waitforbuttonpress()
	run_display(states[7360:], 1, 7360)
	plt.waitforbuttonpress()


def run_display(states, delay, offset):
	for i, state in enumerate(states):
		ax.clear()
		ax.imshow(state[0], cmap=cmap, norm=norm)
		ax.set_title(str(i+offset+1) + " seconds\n" + str(state[2]) + " entropy")
		plt.pause(delay)


def run_only_key(states, delay, offset):
	for i, state in enumerate(states):
		if state[1]:
			ax.clear()
			ax.imshow(state[0], cmap=cmap, norm=norm)
			ax.set_title(str(i+offset+1) + " seconds\n" + str(state[2]) + " entropy")
			plt.pause(delay)


if __name__ == '__main__':
	# set up the grid
	_, ax = plt.subplots(figsize=(13, 11))
	boundaries = [0, 1, 2, 3, 5, 100, 99999]
	colors = ["white", "blue", "green", "orange", "red", "black"]
	cmap = ListedColormap(colors)
	norm = BoundaryNorm(boundaries, cmap.N)
	main()

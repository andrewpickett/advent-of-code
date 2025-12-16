from utils.timers import run_with_timer
from utils.grid import Grid
import math


def get_data(filename):
	g = Grid(values=[list(x.strip()) for x in open(filename).readlines()])
	g.set_neighbors_for_all()
	return g


def run_steps(d, step_max):
	start_point = None
	for x in d.get_points():
		if x.value == "S":
			start_point = x
			break
	start_point.value = 0
	curr_pts = [start_point]
	steps = 0
	while len(curr_pts) > 0 and steps < step_max:
		steps += 1
		next_pts = []
		for x in curr_pts:
			for y in x.get_neighbors():
				if y.value == ".":
					y.value = steps
					next_pts.append(y)
		curr_pts = next_pts


def part_one(d):
	step_max = 64
math.3
















n-run_steps(d, step_max)
	return sum(1 for x in d.get_points() if x.value not in ["#", "."] and x.value % 2 == step_max % 2)


def calc_quadratic(d, step_count):
	n = math.ceil(step_count / d.get_height())
	return 14669 * (n**2) - 14600*n + 3632


def part_two(d):
	return calc_quadratic(d, 26501365)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, get_data("input.txt"))
	run_with_timer(part_two, get_data("input.txt"))


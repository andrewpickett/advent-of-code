from utils.timers import run_with_timer, get_data_with_timer
from utils.algorithms import bfs
from utils.grid import Grid
from itertools import permutations


def get_data(filename):
	d = [x.strip() for x in open(filename).readlines()]
	pts = []
	for x in d:
		pts.append(list(x))
	g = Grid(values=pts)
	g.set_neighbors_for_all()

	points = {}
	for x in g.get_points():
		if x.value not in [".", "#"]:
			points[int(x.value)] = {"p": x, "d": {int(x.value): 0}}

	for x in points:
		for y in points:
			if x != y:
				points[x]["d"][y] = bfs(points[x]["p"], points[y]["p"], lambda t: [z for z in t[0].get_neighbors() if z.value != "#"])[1]
	return points


def calc_min_path(points, return_home=False):
	perms = list(permutations([x for x in points.keys() if x != 0]))
	min_dist = float("inf")
	for x in perms:
		curr_dist = 0
		new_perm = [0] + list(x)
		if return_home:
			new_perm = new_perm + [0]
		for i in range(len(new_perm) - 1):
			curr_dist += points[new_perm[i]]["d"][new_perm[i+1]]
		min_dist = min(min_dist, curr_dist)
	return min_dist


def part_one(d):
	return calc_min_path(d)


def part_two(d):
	return calc_min_path(d, True)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()
